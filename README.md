# Monthly petroleum based product market prices

## Description

This project demonstrates the usage of using Python to extract, transform, and load data. We pulled data from [eis.gov](www.eis.gov).

## Project Administration
[Atlasian page](https://dataengineerproject.atlassian.net/wiki/spaces/DPG/overview)<br>
[Jira board](https://dataengineerproject.atlassian.net/jira/software/projects/DPG/boards/1)<br>
[Lucid chart](https://lucid.app/lucidchart/4b425887-b190-4d5f-b822-7e885d9269b4/edit?beaconFlowId=D2D9FA805D3E468C&invitationId=inv_f134d3d7-dd4c-4d63-b11c-4ece0c4d502e&page=0_0#)<br>
[Documentation of completed requirements](https://dataengineerproject.atlassian.net/wiki/spaces/~55705847a003daa7a04d90acfed162590a0dcc/database/2195458?savedViewId=7ff645f9-55ab-4e30-92de-969cd26175d2)<br>

## Getting Started

### How to run
1. Acquire API key from [eis.gov](www.eis.gov)
2. Optionally build an image and store in Docker Desktop or AWS ECS
3. If you would like to run locally:
  1. Navigate to DEC-project-1 folder
  2. Open terminal and execute:
```bash
python -m etl_project.pipelines.petroleum_data_pull
```
If run successfully, user will see log events in the terminal and records in your database.   

### Dependencies

* All Python dependencies are in the requirements.txt
* AWS account
* API key from [eis.gov](www.eis.gov)
* working databases
  * energy
  * logging

## Authors
Stepheny Agbara
Kat Janyawadee
Jake Shivers

## Version History
* 0.1 (Initial Release)

## License

No need for a license.

## Acknowledgments
### Data Engineer Camp Professors<br>
Doug F <br>
Chris Dilinger <br>
Jay Ng <br>
  
