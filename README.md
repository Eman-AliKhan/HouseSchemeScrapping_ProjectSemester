# 🏡 House Scheme Scraping & Real Estate Data Analysis

A Python-based semester project focused on collecting and analyzing real-estate listing data. The project uses web scraping to gather housing information, organizes the collected data into a structured CSV dataset, and explores interactive dashboard development using Streamlit and Flask.

## 📌 Project Overview

Real-estate listings contain useful information about property prices, locations, and house characteristics. Collecting this information into a structured dataset can make it easier to explore property listings and compare available housing options.

This project focuses on housing data from Peshawar, Pakistan. It demonstrates a practical workflow involving web scraping, data organization, preprocessing, and the development of interfaces for exploring real-estate information.

## 🎯 Objectives

- Collect housing and property information from online real-estate listings.
- Extract relevant property attributes, such as price, location, and number of rooms, where available.
- Store the collected information in a structured CSV dataset.
- Prepare the data for inspection, cleaning, and analysis.
- Explore interactive dashboard development using Streamlit and Flask.
- Understand how Python-based tools can support real-estate data analysis.

## ✨ Key Features

### 🕸️ Web Scraping
Python scripts for collecting property information from online real-estate sources.

### 📊 Structured Housing Dataset
The collected data is stored in CSV format for easier inspection and further processing.

### 🧹 Data Processing
The project workflow includes organizing and cleaning collected property data to improve its usability for analysis.

### 🏘️ Real-Estate Data Exploration
The dataset can support comparisons of property attributes, such as prices, locations, and room counts, depending on the fields available.

### 🖥️ Dashboard Development
The project explores dashboard development using Streamlit and Flask. These frameworks provide different approaches to building Python-based web interfaces.

## 🛠️ Technologies Used

- **Python** — Main programming language
- **Web Scraping** — Collecting real-estate listing information
- **Pandas** — Data processing, if used in the implementation
- **CSV** — Structured data storage
- **Streamlit** — Interactive data application development
- **Flask** — Python web application development

## 📁 Repository Structure

| File | Description |
|---|---|
| `ai_webscrap.py` | Python script associated with the web-scraping workflow |
| `aipro_1.py` | Additional Python project script |
| `zameen_peshawar_houses.csv` | Housing dataset associated with Peshawar property listings |
| `Project overview.pdf` | Project overview and supporting documentation |

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or later
- pip
- The Python packages required by the project scripts

### 1. Clone the Repository

```bash
git clone https://github.com/Eman-AliKhan/HouseSchemeScrapping_ProjectSemester.git
cd HouseSchemeScrapping_ProjectSemester
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the libraries required by the scripts. For example, if the project uses these packages:

```bash
pip install requests beautifulsoup4 pandas streamlit flask
```

The exact dependencies depend on the imports and implementation in the Python files.

### 4. Explore the Dataset

Open `zameen_peshawar_houses.csv` in a spreadsheet application or load it with Python for inspection and analysis.

Example using Pandas:

```python
import pandas as pd

df = pd.read_csv("zameen_peshawar_houses.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
```

### 5. Run the Application

Review the Python scripts to identify their entry points and configuration requirements before running them. For a Streamlit application, the command typically follows this pattern:

```bash
streamlit run ai_webscrap.py
```

Use this command only if `ai_webscrap.py` is the Streamlit entry-point script. The Flask application, if separate, may need to be started differently.

## 📈 Potential Applications

- Exploring housing listings in Peshawar
- Comparing property prices across locations
- Investigating relationships between property characteristics and prices
- Preparing real-estate datasets for visualization and further analysis
- Prototyping data-driven tools for housing-market exploration

## 🎓 Learning Outcomes

This project provides practical experience with:

- Web scraping and data collection
- Structured dataset creation
- Data cleaning and preprocessing
- Python-based data applications
- Streamlit and Flask development approaches
- Applying data analysis techniques to a real-world domain

## 👩‍💻 Author

**Eman Ali Khan**

GitHub: [@Eman-AliKhan](https://github.com/Eman-AliKhan)

## 📚 Project Information

**Type:** Academic Semester Project  
**Domain:** Web Scraping, Real Estate Data, and Data Analysis  
**Geographic Focus:** Peshawar, Pakistan

---

*This project demonstrates a practical approach to collecting and organizing real-estate data for analysis and application development.*
