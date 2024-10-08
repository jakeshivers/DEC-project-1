# Project Overview

## Project Context & Goals
This project was designed to implement an ELT pipeline that extracts monthly petroleum based product market prices from [eis.gov](www.eis.gov), loads the processed data into AWS and transforms it according to specified requirements.

Our key goals included:

<li>Extracting data demonstrating ability to handle both live and static datasets<br>
<li>Perform data transformations according to requirements (showing 7 transformation techniques)<br>
<li>Deploying the pipeline in a containerized environment on AWS <br>
<li>Demonstrate collaboration by using GitHub for parallel coding and Jira for progress tracking


## Team Members
<li>Stepheny Agbara<br>
<li>Kat Janyawadee<br>
<li>Jake Shivers

## Project Administration
[Atlasian page](https://dataengineerproject.atlassian.net/wiki/spaces/DPG/overview)<br>
[Jira board](https://dataengineerproject.atlassian.net/jira/software/projects/DPG/boards/1)<br>
[Lucid chart](https://lucid.app/lucidchart/4b425887-b190-4d5f-b822-7e885d9269b4/edit?beaconFlowId=D2D9FA805D3E468C&invitationId=inv_f134d3d7-dd4c-4d63-b11c-4ece0c4d502e&page=0_0#)<br>
[Documentation of completed requirements](https://dataengineerproject.atlassian.net/wiki/spaces/~55705847a003daa7a04d90acfed162590a0dcc/database/2195458?savedViewId=7ff645f9-55ab-4e30-92de-969cd26175d2)<br>

## Git for Collaboration
We used Git for version control, collaborating through:
<li>Git commits and push<br>
<li>Creating seperate branches for each work stream <br>
<li>Opening pull requests for code reviews <br>

<br>
<br>
<br>


# Solution Architecture Diagram
We have designed our solution following an ETL approach. Below is a simplified view of our architecture:<br><br>
![image](https://github.com/user-attachments/assets/1671eb03-907e-4d63-a91a-81d51e2a86d5)<br><br>

### Components
* Data Sources: Live API and static CSV.<br>
* ELT Pipeline:
  * Extract: Fetched data from both the live API and the static CSV.
  * Load: Stored processed data in a relational database and S3 bucket
  * Transform: Applied transformations such as filtering, aggregation, and data type conversions.<br>
* AWS:<br>
  * Deployed the pipeline using ECS, ECR, and RDS/S3.


### Dependencies
* All Python dependencies are in the requirements.txt
* AWS account
* API key from [eis.gov](www.eis.gov)
* working databases
  * energy
  * logging<br>

<br>
<br>
<br>



# ELT

## Extract

### Dataset Selected
We used a periodically updated live dataset containing petroleum data from a public API - [eis.gov](www.eis.gov). We also worked with a static dataset (country.csv) containing country data for transformation purposes. This approach allowed us to demonstrate extraction and transformation techniques.

## Load
Using AWS and Postgres, we were able to load the extracted data into a database.<br>
  * ECS
![ECS](https://github.com/user-attachments/assets/05ed7e1b-a3ba-450d-9b86-295cf46bdb5a)<br><br>
  * ECR
![ECS Cluster](https://github.com/user-attachments/assets/6d48bce4-b26b-496a-a1ba-a050e885482b)<br><br>
  * Logs
![Logs](https://github.com/user-attachments/assets/4c519f3b-3e86-4848-8590-e5adadb6a77e)<br><br>
  * RDS
![RDS](https://github.com/user-attachments/assets/df30dc08-3972-4f3e-b5b6-403c47628262)<br><br>
  * S3
![image](https://github.com/user-attachments/assets/b0c6488a-c7e2-4be2-befc-2e9dcb6c2654)<br><br>


## Transform
We performed the following transformations
### Transformation 1 -> Renaming
![Transformation - Renaming Columns](Images/Transformation%20-%20Renaming%20Columns.png)
### Transformation 2 -> Datatype Casting
![Transformation - Datatype Change](Images/Transformation%20-%20Datatype%20Change.png)
### Transformation 3 -> Sorting
![Transformation - Sorting](Images/Transformation%20-%20Sorting.png)
### Transformation 4 -> Filtering
![Transformation - Filtering](Images/Transformation%20-%20Filtering.png)
### Transformation 5 -> Joins/Merges
![Transformation - Merge](Images/Transformation%20-%20Merge.png)
### Transformation 6 & 7 -> Grouping + Aggregation
Here we performed 2 transformations - grouping and aggregation - together.
![Transformation - Grouping](Images/Transformation%20-%20Grouping.png)


<br>
<br>
<br>


# Lessons Learned
Throughout this project, we gained valuable insights into the challenges and best practices of building an end-to-end data pipeline, most important:

* The value of attention to detail in data engineering: We had 2 scenarios where we could have saved troubleshooting time by paying keener attention to details
  * Moving from local environment to Docker (local) to AWS containers requires a bit of attention to detail. We struggled hopping from one environment to another until we realized the .env files were not the same in one of the three environments.
  * While troubleshooting, we were querying the wrong database. Our app was running, but we kept refreshing an empty (and incorrect) DB!


## Version History
* 0.1 (Initial Release)

## License

No need for a license.

## Acknowledgments
### Data Engineer Camp Professors<br>
Doug F <br>
Chris Dilinger <br>
Jay Ng <br>