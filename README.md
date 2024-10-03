# Monthly petroleum based product market prices

## Description, context and goals.

This project demonstrates the usage of using Python to extract, transform, and load data. The project is hosted in a container on AWS.
We pulled data from [eis.gov](www.eis.gov). We used the API data to track and compare historical petroleum products over the course of the year.

## Project Administration
[Atlasian page](https://dataengineerproject.atlassian.net/wiki/spaces/DPG/overview)<br>
[Jira board](https://dataengineerproject.atlassian.net/jira/software/projects/DPG/boards/1)<br>
[Lucid chart](https://lucid.app/lucidchart/4b425887-b190-4d5f-b822-7e885d9269b4/edit?beaconFlowId=D2D9FA805D3E468C&invitationId=inv_f134d3d7-dd4c-4d63-b11c-4ece0c4d502e&page=0_0#)<br>
[Documentation of completed requirements](https://dataengineerproject.atlassian.net/wiki/spaces/~55705847a003daa7a04d90acfed162590a0dcc/database/2195458?savedViewId=7ff645f9-55ab-4e30-92de-969cd26175d2)<br>

## Getting Started

### How to run
1. Acquire API key from [eis.gov](www.eis.gov)
2. Add `.env` file to your solution (see below for parameter names)
3. Optionally build an image and store in Docker Desktop or AWS ECS
4. If you would like to run locally:
  1. Navigate to DEC-project-1 folder
  2. Open terminal and execute:
```python
python -m etl_project.pipelines.petroleum_data_pull
```
If run successfully, user will see log events in the terminal and records in your database.   

#### Configuration of `.env` file
```env
API_KEY=<get this from www.eis.gov>

#Database
SERVER_NAME=<server name> 
DATABASE_NAME=energy
DB_USERNAME=<db name>
DB_PASSWORD=<db pw>
PORT=<port> #most likely 5432

#Logging to DB
LOGGING_SERVER_NAME=<server name> 
LOGGING_DATABASE_NAME=energy
LOGGING_DB_USERNAME=<db name>
LOGGING_DB_PASSWORD=<db pw>
LOGGING_PORT=<port> #most likely 5432

```


### Dependencies

* All Python dependencies are in the requirements.txt
* AWS account
* API key from [eis.gov](www.eis.gov)
* working databases
  * energy
  * logging

## Solution Architecture
* Python
* Postgres Database
* AWS:
  * Docker
  * ECR
  * S3: stores the `.env` file
    
## Lessons Learned
Moving from local environment to Docker (local) to AWS containers requires a bit of attention to detail. We struggled hopping from one environment to another until we realized the .env files were not the same in one of the three environments. Additionally, while troubleshooting, we were querying the wrong database. Our app was running, but we kept refreshing an empty (and incorrect) DB! You must pay attention to which environment you're focus is on.

## Authors
Stepheny Agbara<br>
Kat Janyawadee<br>
Jake Shivers<br>

# AWS Environment
### ECS
![ECS](https://github.com/user-attachments/assets/05ed7e1b-a3ba-450d-9b86-295cf46bdb5a)

### ECR
![ECS Cluster](https://github.com/user-attachments/assets/6d48bce4-b26b-496a-a1ba-a050e885482b)

### Logs
![Logs](https://github.com/user-attachments/assets/4c519f3b-3e86-4848-8590-e5adadb6a77e)


### RDS
![RDS](https://github.com/user-attachments/assets/df30dc08-3972-4f3e-b5b6-403c47628262)

### S3
![image](https://github.com/user-attachments/assets/b0c6488a-c7e2-4be2-befc-2e9dcb6c2654)

## Version History
* 0.1 (Initial Release)

## License

No need for a license.

## Acknowledgments
### Data Engineer Camp Professors<br>
Doug F <br>
Chris Dilinger <br>
Jay Ng <br>
  
