# TigerGraph SE Demo Pack Installer v1.2
## 

`tgSEDemoPack` - this package contains the content required to populate any TigerGraph instance (local/cloud/tgcloud) with custom SE demo content and/or any of the 26 Starter Kits available on TGCloud. The current version provides the following content:
    
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

## Installation

To Install any of the content, follow these steps:

1. Clone this project, which contains the tgSEDemoPack.tar.gz package. The project can be cloned to your local environment, or directly to a target platform (EC2)

    git clone https://github.com/TigerGraph-DevLabs/tgSEDemoPack.git

2.  (Optional) Custom demo data is provided via a seperate archie, download the data file archieve using the follwoing command. Note: this public S3 bucket location may change some day

    ```bash
    cd <path>/tgSEDemoPack
    cd ..
    wget https://tgsedemodatabucket.s3.amazonaws.com/tgSEDemoPackData.tar.gz
    tar -xzf tgSEDemoPackData.tar.gz
    ```

3. Pre-requisites - As with any good utility, preperation is key. tgSolution pack is dependent on a couple things:

   Run the pre-requisite check to ensure your environment is ready

    ```bash
    cd tgSEDemoPack
   ./checkPreReqs.sh
    ```

<ol>
<li>For TGCloud install, Python 3 is required</li>
<li>For TGCloud install, pyTigerGraph package must be installed (pip install pyTigerGraph)</li>
<li>For a Starter kit install, data is loaded from a private S3 bucket and requires an access token valid with the tgSales account</li>
<li>For local install, just make sure Tigergraph is installed and services are running on the host</li>

  NOTE: In order to load source data efficiently, it has been staged onto an S3 bucket. You will need an AWS client key/secret to connect to the bucket via python, which looks like this:

    Access key ID,Secret access key
    **************QOC7EB,**************************oCbLPdAZ

4. Execute the installer:

    ```bash
    ./runTGSInstall.sh
    ```

    Follow the prompts to:

Welcome to the TGSolution Pack Installer.....
  This package will install TigerGraph modules (graph and data) onto any install
  of TigerGraph - local/EC2/TGCloud

Would you like to install a Customer Demo or a TigerGraph Starter Kit?

  Enter Custom Demo/Starter Kit - C/c/S/s: s

This installer will install any starter kit on any tg instance

Install options are:
   1. GSQL - Install via gsql command line to a local
   3. Python - Install via python script and pyTigerGraph library to a remote instance

     NOTE: Setup on TGCloud is only available thru python install

  1   -  AML 
  2   -  CentralityAlgorithms 
  3   -  CommunityDetection 
  4   -  ConvolutionalNetwork 
  5   -  COVID19 
  6   -  Cust360 
  7   -  CyberSecThreatDetection 
  8   -  DataLineage 
  9   -  EnterpriseKnowledgeCorp 
  10  -  EnterpriseKnowledgeCrunchbase 
  11  -  EntityResMDM 
  12  -  FinServPaymentFraud 
  13  -  FraudFinServ 
  14  -  GSQL101 
  15  -  HealthCareFAERS 
  16  -  HealthCareReferrals 
  17  -  InDBBGML 
  18  -  InDBML 
  19  -  LowRankApproxML 
  20  -  ML_RTFraud 
  21  -  NetworkITResourceOptimization 
  22  -  Rec2HyperMarketing 
  23  -  RecEngMovie 
  24  -  ShortestPathAlgorithms 
  25  -  SocialNet 
  26  -  SupplyChain 

choose the kit you want to work with
     Valid kits are 1 thru 27: 7

starter kit choosen is:  7
 corresponding to kit:  CyberSecThreatDetection

What would you like to do today?
   C/c - create kit schema
   D/d - create the S3 data source - NOTE: in order to load data, you need a data source
   L/l - create a load job for a kit
   R/r - run a load job
   A/a - Do all 3, create schema and job, and run load for a kit

Do you want to install via GSQL or Python? (G/P/p): p
Cool, python it is...
Lets make sure python is installed and configured
Python 3.9.10
Python installed, checking version
Update the connection props...

The current property settings are:

tg_host = https://gsql101-lab-bob.i.tgcloud.io
tg_username = tigergraph
tg_password = TigerG123
tg_s3_data_source = tg_s3_data_source
tg_s3_bucket_name = tg-workshop-us
tg_access_key_ID = ************QOC7EB
tg_secret_access_key = ***********************oCbLPdAZ

5. The tgSEDemoPack come with two types of content

    a. Custom demo packages described above - The custom Demos load local data from the tgSEDemoPackData.tar.gz archive
        also available on S3, please download it and add to your tgSEDemoPack file structure (step 2 above)
    b. Install a Starter Kit also decribed above

6. There are multiple ways to run the installer for maximum flexibility, you can clone repo:

    a. Directly to the Tigergraph server, run gsql scripts locally
    b. To any EC2 instance, run python scripts from there
    c. To your Mac, and run either
        c1. Python scripts to connect to TGCloud
        c2. GSQL scripts to connect to Docker on localhost 

The package can be installed on any instance running the TigerGraph application. 
The install process is simple:

7.  Select one of the solution packs to install

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

8.  The script will create the objects, loading job and execute each load job to populate the graph.

9.  Go to the Studio UI to see progress
    -   for the local Docker container: <http://localhost:14240>

    - The demo pack can also install mysql-based schema into a local mysql database
    - future releases of the demo pack will include Data packs of various sizes: small, large, gi-normous

