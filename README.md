# TigerGraph SE Demo Pack Installer v1.2
## 

`tgSEDemoPack` - this package contains the content required to populate any TigerGraph instance (local/cloud/tgcloud). The current version includes the following content:
    
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

1. Clone this project, which contains the tgSEDemoPack.tar.gz package. The project can be cloned to your local environment, or directly to a target platform (EC2/GCE/etc..)

    git clone https://github.com/TigerGraph-DevLabs/tgSEDemoPack.git

2. Execute the demo pack installer with 

    ```bash
    cd tgSEDemoPack
   ./runTGSInstall.sh
    ```

3. The installer will perform a few verification steps the first time it is run. These include:

<ol>
<li>For TGCloud install, Python 3 is required</li>
<li>For TGCloud install, pyTigerGraph package must be installed (pip install pyTigerGraph)</li>
<li>For a Starter kit install, data is loaded from a private S3 bucket and requires an access token valid with the tgSales account</li>
<li>For local install, just make sure Tigergraph is installed and services are running on the host</li>

  For the Starter Kits, source data is staged onto an S3 bucket. This bucket is private and will require an AWS client key/secret to connect to the bucket via python, which looks like this:

    Access key ID,Secret access key
    **************QOC7EB,**************************oCbLPdAZ

4. Follow the prompts to:

    a) Install one of more (all) custom demos.
    b) Install one of more starter kits

5. You can install ALL of the starter kits at once by running the below scripts:

    ```bash
    cd tgSEDemoPack
    ./checkPreReqs.sh
    ./setProps.sh
    nohup ./createAllSchemas_Unattended.sh > tgSEDemoPack.out 2>&1 &
    ```

    NOTE: Running the Unattended version of the installer unsures that the gsql/python commands will run successfully, as data load can often take 10-15min, and if the shell session running is ended
          during this time the script with stop.

Here are the properties used to execute the the installer

        tg_host = https://gsql101-lab-bob.i.tgcloud.io
        tg_username = tigergraph
        tg_password = TigerG123
        tg_s3_data_source = tg_s3_data_source
        tg_s3_bucket_name = tg-workshop-us
        tg_access_key_ID = ************QOC7EB
        tg_secret_access_key = ***********************oCbLPdAZ

6. There are multiple ways to deploy the installer for maximum flexibility, you can clone repo:

    a. Directly to the Tigergraph server, run gsql scripts from the server as the tigergraph user
    b. To any EC2 instance, run python scripts from there and install remotely
    c. To your Mac, and run either
        c1. Python scripts to connect to TGCloud or other VM
        c2. GSQL scripts to connect to Docker on localhost 

8.  The script will create the schema, loading job and execute each load job to populate the graph. To add new kits to the Deployer, simply

    Create 3 gsql scripts
        - Create all schema objects (create-schema-<pack name>.gsql)
        - Create load job (create-load-job-<pack name>.gsql)
        - Run Load job (run-load-job-<pack name>.gsql)

        In the load job definition, use the S3 loader syntax and place your source files on S3. Something like this:

        LOAD "$tg_s3_data_source:{\"file.uris\":\"s3://tg-workshop-us/starter-kits/HealthCareFAERS/ReportedCase.tsv\"}" TO VERTEX ReportedCase VALUES ($"primary_id", $"caseid", $"caseversion", $"fda_dt", $"mfr_sndr", $"reporter_country", $"occr_country") USING SEPARATOR = "\t", HEADER = "true";

9.  Go to the Studio UI to see progress
    -   for the local Docker container: <http://localhost:14240>

10. Roadmap

    - The demo pack can also install mysql-based schema into a local mysql database
    - future releases of the demo pack will include Data packs of various sizes: small, large, gi-normous
    - Queries are not yet packaged with the installer
    

