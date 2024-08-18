# WebScraping - Wikipedia (About Countries)

## Table of Contents
* [Introduction](#Introduction)
* [Technologies](#technologies)
* [Setup](#setup)
* [Refences](#references)

## Introduction
This project we undertake a data engineering task in conjuction with software engineering to full automate data collaction and data storage process.

### Project overview

* Data Collection
Through the API we shall select specific informationneeded for the project.

* Data Storage
After data collection, using the database created for this projects, we chose Postgres to store our data.

* Automation
Using Airflow a daily task will be scheduled to pull the data from the API and store it in the Database.

* Data Presentation 
From the API built by us, in a table format this information will be displayed on a website

## Technologies
This project is built using 

*Python 3.*+
*HTML, CSS, JavaScript

## Setup 
For this project to run successfully ensure python and and pyspark is intalled
```
    To install python - brew install python for mac users
    To install pyspark - pip3 install pyspark/pip install pyspark
```

## References
https://www.crummy.com/software/BeautifulSoup/bs4/doc/