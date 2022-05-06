# Overview

This document and corresponding video will allow you to set up a Synthea Analysis demo in Kubernetes

To find one quick method to bring up a Kubernetes on the 3 major cloud platforms, please refer to this GitHub document

-   [Provision managed Kubernetes in cloud platforms · gregoryg/homelab · GitHub](https://github.com/gregoryg/homelab/blob/master/cloud-provisioning/provision-vms.org#provision-managed-kubernetes-in-cloud-platforms)

    We are going to bring up an AKS (Microsoft Azure) cluster, deploy a 4-node TigerGraph cluster in Kubernetes, and "hydrate" the Synthea demo in its entirety from only the GSQL scripts and the compressed data.

    Additionally, we will split the input data to facilitate parallel loading. This step in practice is very optional - it may not be worth the effort if you are not explicitly demonstrating the power of parallel loading to your prospect.


# Provision Kubernetes cluster

The first step is to bring up a Kubernetes cluster. If you already have one running, skip this step!

From the provisioning example linked above, we excerpt the following command line. For what it's worth, I find provisioning Kubernetes clusters from any of the cloud platform web consoles to be **more** confusing and time-consuming than the command line.


## Scripts

-   ref: [Quickstart: Deploy an AKS cluster by using Azure CLI - Azure Kubernetes Servi&#x2026;](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough)

    ```bash
    # create resource group
    az group create --name synthea-aks-rg --location eastus
    ```
-   Assure cluster monitoring is ready to go

    ```bash
    az provider show -n Microsoft.OperationsManagement -o table
    az provider show -n Microsoft.OperationalInsights -o table
    ## If not already registered - then register!
    az provider register --namespace Microsoft.OperationsManagement
    az provider register --namespace Microsoft.OperationalInsights
    ```
-   Create AKS cluster

    ```bash
    ##   --generate-ssh-keys \
    az aks create \
       --name synthea-tiger35 \
       --resource-group synthea-aks-rg \
       --node-count 4 \
       --enable-addons monitoring \
       --ssh-key-value ~/.ssh/azure_gg-tg_key.pub \
       --admin-username gregj \
       --node-vm-size Standard_DS4_v2
    ```
-   Install `kubectl` using Azure (optional if you already have `kubectl`)

    ```bash
    az aks install-cli
    ```
-   Nab credentials Be careful here, as the following command will overwrite your existing `~/.kube/config` file if you have one. Use a variation of the second command otherwise, or merge

    -   ref: [az aks get-credentials | Microsoft Docs](https://docs.microsoft.com/en-US/cli/azure/aks?view=azure-cli-latest#az-aks-get-credentials)

    ```bash
    az aks get-credentials --resource-group synthea-aks-rg --name synthea-tiger35 --overwrite-existing
    # example of creating a separate kubeconfig file instead of overwriting the default
    # az aks get-credentials --resource-group synthea-aks-rg --name synthea-tiger35 --file - > ~/.kube/config-files/aks-synthea-demo.yaml
    ```


# A detour showing some Kubernetes control commands

Kubernetes commands to get you started, some nice shortcuts, and a curses-based tool to help out!

Now that you have your `kubectl` command installed


## Set up useful aliases and completion in ~/.bashrc

Keep in mind this functionality is available using `zsh` also

```bash
alias k='kubectl'
alias kn='kubectl config set-context --current --namespace '
alias kx='kubectl config get-contexts'
## Kubernetes completion
source <(kubectl completion bash)
complete -F __start_kubectl k
```


# Deploy TigerGraph

-   Ref: [Kubernetes - TigerGraph Docs](https://docs.tigergraph.com/tigergraph-server/current/kubernetes/)

Currently the deployment method uses a shell script and Kustomize to create a deployment manifest as a BBOY (big blob of YAML). Hopefully for the love of Pete we will soon have a Helm deployment.

For a sneak peek of what it will look like on the glorious day there **is** a Helm deployment, check out my demo video: [TigerGraph in Rancher Catalog - YouTube](https://www.youtube.com/watch?v=Gpsb7uP3xmU)

```bash
git clone https://github.com/tigergraph/ecosys
cd ecosys/k8s
```

```bash
./tg aks kustomize -n tigergraph --size 4 -v 3.5.1 --pv 350 --cpu 4 --mem 8
kubectl create ns tigergraph
kubectl apply -f deploy/tigergraph-aks-tigergraph.yaml
```

Watch progress using `kubectl` or `k9s`


# Get a shell in the "m1" container of the TigerGraph deployment

Most of what happens from here on will be done in the `m1` server node - the `tigergraph-0` pod in this case.

```bash
kubectl -n tigergraph exec -it -- bash
```


# Copy the compressed data files

At this moment I have data and scripts stored on a Google Cloud Storage bucket. So this step will get us access to GCS and copy the files over.


## Google Cloud CLI

-   ref: [Installing the gcloud CLI  |  Google Cloud](https://cloud.google.com/sdk/docs/install)

```bash
sudo apt update && sudo apt -y install python3
cd ~
curl -k -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-371.0.0-linux-x86_64.tar.gz
tar xf google-cloud-sdk-371.0.0-linux-x86_64.tar.gz
rm -v google-cloud-sdk-371.0.0-linux-x86_64.tar.gz
echo 'export PATH=$PATH:~/google-cloud-sdk/bin' >> ~/.bashrc
source ~/.bashrc
gcloud auth login
gcloud config set project tigergraph-sales
```


## Copy and decompress the files

```bash
gsutil -m cp -r  gs://tg-demo-gcs/synthea ~/mydata/
cd ~/mydata/synthea/data/csv
gunzip -v *gz
```

Result:

    conditions-with-id.csv.gz:	 78.3% -- replaced with conditions-with-id.csv
    encounters.csv.gz:	 84.6% -- replaced with encounters.csv
    medications.csv.gz:	 87.8% -- replaced with medications.csv
    organizations.csv.gz:	 68.2% -- replaced with organizations.csv
    patients.csv.gz:	 60.5% -- replaced with patients.csv
    procedures-with-id.csv.gz:	 88.4% -- replaced with procedures-with-id.csv
    providers.csv.gz:	 61.4% -- replaced with providers.csv
    tigergraph@tigergraph-0:~/mydata/synthea/data/csv$ ls -lh
    total 103G
    -rw-r--r-- 1 tigergraph tigergraph 9.3G May  5 18:04 conditions-with-id.csv
    -rw-r--r-- 1 tigergraph tigergraph  33G May  5 18:05 encounters.csv
    -rw-r--r-- 1 tigergraph tigergraph  22G May  5 18:05 medications.csv
    -rw-r--r-- 1 tigergraph tigergraph 218K May  5 18:04 organizations.csv
    -rw-r--r-- 1 tigergraph tigergraph 602M May  5 18:04 patients.csv
    -rw-r--r-- 1 tigergraph tigergraph  39G May  5 18:05 procedures-with-id.csv
    -rw-r--r-- 1 tigergraph tigergraph 269K May  5 18:04 providers.csv
    tigergraph@tigergraph-0:~/mydata/synthea/data/csv$ du -sh
    103G	.


# Split file loads


## Split them files

```bash
# Set NUM_SPLITS to an explicit count if different from number of TigerGraph nodes
if [[ ! -v NUM_SPLITS &&  $(which gadmin) ]]; then
    NUM_SPLITS=$(gadmin config get System.HostList | jq -r '. | length')
else
    NUM_SPLITS=${NUM_SPLITS:-3}
fi
echo "Splitting CSV files into ${NUM_SPLITS} parts"
for i in *csv; do
    prefix=$(echo $i | sed 's,\.csv,,')
    echo $prefix
    split --numeric-suffixes=0 -n l/${NUM_SPLITS} $i $prefix
done
```


## Generate `DEFINE HEADER` GSQL for use in loading jobs

```bash
# # Add header in to files (very slow)
# for i in *00; do
#     filebase=$(echo $i | sed 's,00$,,')
#     header=$(head -1 $i)
#     echo "Adding header to $filebase files"
#     sed -i "1i$header" "${filebase}"0[1-9]
# done
# Save header off in separate file, remove header from first split
rm -f headers-snippet.gsql
for i in *00; do
    filebase=$(echo ${i} | sed 's,[0-9]\{2\}$,,')
    echo "Writing header file for ${i}"
    head -1 "${i}" | sed 's!\(.\+\)!  DEFINE HEADER hdr_'${filebase}' = "\1"\;!' | sed 's!,!","!g' | tee -a headers-snippet.gsql
done
echo "Removing header from initial splits"
for i in *00; do
    tail -n +2 ${i} > ${i}.tmp
    mv -v ${i}.tmp ${i}
done
```


## Copy the split files to their appropriate nodes

```bash
# Take one split file with filename ending in 2 digits like myfile00 -
# move that file to TigerGraph node m{num+1}:mydata/synthea/data/split/myfile.csv
# This script can then be used with GNU parallel as
# parallel --gnu move-split-file.sh ::: *[0-9][0-9]
# Use gscp on TigerGraph installations
# Move file as-is to remote node, then rename using gssh to avoid unwanted directory creation
i=$1

if [[ ! -v NUM_NODES && $(which gadmin) ]]; then
    NUM_NODES=$(gadmin config get System.HostList | jq -r '. | length')
else
    NUM_NODES=${NUM_NODES:-3}
    echo "This script is meant to be run as user tigergraph on a tigergraph cluster node -- stopping"
    exit 1
fi
# for i in  *0[0-9]; do
    filename=$(echo $i | sed 's,0[0-9]$,.csv,')
    nodeidx=$(echo $i | sed 's,.\+\([0-9]\),\1,')
    nodeID=$(gadmin config get System.HostList | jq -r '.['${nodeidx}'].ID')
    echo "Copying $i to $filename on node ${nodeID}"
    gscp ${nodeID} ${i} mydata/synthea/data/split/
    gssh ${nodeID} mv -v mydata/synthea/data/split/${i} mydata/synthea/data/split/${filename}
    # rm -v ${i}
# done
```


# Run GSQL Schema creation, data load and query installation

```bash
cd ~/mydata/synthea/gsql
gsql 01_create_schema_change_job_SyntheaAnalysis.gsql
gsql 02_create_load_jobs_SyntheaAnalysis_stage.gsql
gsql 03_install_queries_SyntheaAnalysis.gsql
```


# Nuke the AKS cluster when all is done

You may nuke the cluster by deleting the resource group (love Azure)

```bash
az group delete --name synthea-aks-rg --yes --no-wait
```