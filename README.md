# TigerGraph Solution Pack Installer v1.2
## 

`tgSolutionPack` - this package contains the content required to populate any TigerGraph instance (local/cloud/tgcloud) with custom SE demo content and/or any of the 26 Starter Kits available on TGCloud. The current version provides the following content:
    
## Custom Demos 
### These demos cover various public datasets (LDBC, TPC, Synthea) and other general purpose TG solutions.

<ol>
<li>Entity Resolution(MDM)</li>
<li>Fraud Detection</li>
<li>LDBC Benchmark</li>
<li>TPC-DS Benchmark</li>
<li>Synthea HealthCare</li>
<li>IMDB</li>
<li>Customer360</li>
<li>Recommendations</li>
<li>AML Sim</li>
<li>Ontime Flight Performance</li>
<li>Adworks</li>
</ol>

## Starter Kits
### All 26 of the published TGCLoud templates (known as Starter Kits) are included. This repo is then integrated into the starter kit release cycle.

<ol>
<li>AML</li>
<li>COVID19</li>
<li>CentralityAlgorithms</li>
<li>CommunityDetection</li>
<li>ConvolutionalNetwork</li>
<li>Cust360</li>
<li>CyberSecThreatDetection</li>
<li>DataLineage</li>
<li>EnterpriseKnowledgeCorp</li>
<li>EnterpriseKnowledgeCrunchbase</li>
<li>EntityResMDM</li>
<li>FinServPaymentFraud</li>
<li>FraudFinServ</li>
<li>GSQL101</li>
<li>HealthCareFAERS</li>
<li>HealthCareReferrals</li>
<li>InDBBGML</li>
<li>InDBML</li>
<li>LowRankApproxML</li>
<li>ML_RTFraud</li>
<li>NetworkITResourceOptimization</li>
<li>Rec2HyperMarketing</li>
<li>RecEngMovie</li>
<li>ShortestPathAlgorithms</li>
<li>SocialNet</li>
<li>SupplyChain
</ol>

## Pre-requisites - As with any good utility, preperation is key. tgSolution pack is dependent on a couple things:

<ol>
<li>For TGCloud install, Python 3 is required</li>
<li>For local install, just make sure Tigergraph is installed and services are running</li>

## Installation

To Install any of the content, follow these steps:

1. Clone this project, which contains the tgSolutionPack.tar.gz package. The project can be cloned to your local environment, or directly to a target platform (EC2)

    git clone https://github.com/TigerGraph-DevLabs/tgSolutionPack.git

2.  (Optional) Custom demo data is provided via a seperate archie, download the data file archieve using the follwoing command. Note: this public S3 bucket location may change some day

    ```bash
    cd <path>/tgSolutionPack
    cd ..
    wget https://tgsedemodatabucket.s3.amazonaws.com/tgSolutionPackData.tar.gz
    tar -xzf tgSolutionPackData.tar.gz
    ```

3.    Cd to the root of the project, and execute the installer:

    ```bash
    cd tgSolutionPack
    ./runTGSInstall.sh
    ```

    Follow the prompts to:

4. The tgSolutionPack come with two types of content

    a. Install a custom demo described above
    b. Install a Starter Kit alos decribed above

4. There are multiple ways to run the installer for maximum flexibility, you can clone repo:

    a. Directly to the Tigergraph server, run gsql scripts locally
    b. To any EC2 instance, run python scripts from there
    c. To your Mac, and run either
        c1. Python scripts to connect to TGCloud
        c2. GSQL scripts to connect to Docker on localhost 



The package can be installed on any instance running a TigerGraph application (Note: TGCLoud install not yet support). 
The install process is simple:

4.  SSH to the container

    ```bash
    ssh -p 14022 tigergraph@localhost
    ```

5.  Uncompress the archive to the `mydata` directory:

    ```bash
    mkdir ~/mydata
    cd mydata
    tar -xzvf ../tgSolutionPack.tar.gz
    tar -xzvf ../tgSolutionPackData.tar.gz
    ```

6.  change directory into the tgSolutionPack folder:

    ```bash
    cd tgSolutionPack
    ```

7.  run the install script and follow the instructions

    ```bash
    ./runTGSInstall.sh
    ```

8.  Select one of the solution packs to install

    1 - Entity Resolution(MDM)
    2 - Fraud Detection
    3 - LDBC Benchmark
    4 - TPC-DS Benchmark
    5 - Synthea HealthCare
    6 - IMDB
    7 - Customer360
    8 - Recommendations
    9 - AML Sim
    10 - Ontime Flight Performance
    11 - Adworks
    A/a - install all of the packs
    mysql - Stage all of the source data to a local mysql db

9.  The script Will create the objects, loading job and execute each load job to populate the graph.

10.  Go to the Studio UI to see progress
    -   for the local Docker container: <http://localhost:14240>

The TGSolution Pack also includes copies of every TigerGraph Starter Kit


The Starter Kits are installed using these steps:

1. Run these setConnectionParams.sh script to configure the demo pack to connect to the TigerGraph server

2. Run the installKit.sh script and follow the instructions

Notes

    - The demo pack can also install sql-based schema into a local mysql database
    - future releases of the demo pack will include Data packs of various sizes: small, large, gi-normous

