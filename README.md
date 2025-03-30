# Course Scraper

This project is a web scraper built using Selenium to extract information about online courses from Mate academy. The script collects course descriptions, durations, number of modules and topics, and course types.

## Features

* Uses Selenium WebDriver to interact with the website.
* Extracts key course details such as duration, modules, and topics.
* Saves the extracted data into a JSON file (courses_data.json).

## Technology stack

* Language: Python 3
* A web automation tool: Selenium
* A Python package for automatically managing browser drivers: webdriver_manager
* Storing the scraped data: JSON

## Installation

### Prerequisites

* Python 3.7+
* Google Chrome (latest version recommended)
* ChromeDriver (installed automatically via webdriver-manager)

### Setup

#### Clone this repository:
* git clone https://github.com/oleg-potichnyi/mate-academy-scraper
* cd mate-academy-scraper

#### Install required dependencies: 
* pip install -r requirements.txt

## Usage

### Run the scraper by executing: 
* python main.py

### This will:

* Launch a Chrome browser instance.
* Navigate through the course pages.
* Extract course details.
* Save the data into courses_data.json.
