# Project plan

## Objective

This project will pull historical petroleum price data from the EIS API. We can compare historical prices as well as various peteroleum based products (gasoline, diesel, jet fuel)



## Consumers

The users of our datasets are Data Analysts in the petroleum industry.


## Questions

What questions are you trying to answer with your data? How will your data support your users?

Example:

> - How many orders are there for each customer?
> - What countries and regions have the most orders?
> - What customers have their orders delayed?
> - How many delayed orders are there for each country and region?
> - How many orders do we have for each day?
> - How many delayed orders do we have for each day?

## Source datasets

What datasets are you sourcing from? How frequently are the source datasets updating?

Example:

| Source name | Source type | Source documentation |
| - | - | - |
| Customers database | PostgreSQL database | - |
| Eia API | REST API | [Documentation link](https://www.eia.gov/opendata/browser/petroleum/pri) |

## Solution architecture

How are we going to get data flowing from source to serving? What components and services will we combine to implement the solution? How do we automate the entire running of the solution?

- What data extraction patterns are you going to be using?
- What data loading patterns are you going to be using?
- What data transformation patterns are you going to be performing?

We recommend using a diagramming tool like [draw.io](https://draw.io/) to create your architecture diagram.

Here is a sample solution architecture diagram:

![images/sample-solution-architecture-diagram.png](images/sample-solution-architecture-diagram.png)

## Breakdown of tasks

We will be using the free version of [Jira](https://dataengineerproject.atlassian.net/jira/software/projects/DPG/boards/1) to track out tasks.

