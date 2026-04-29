## Data Seed PH

[![GitHub stars](https://img.shields.io/github/stars/christiangarcia0311/data-seed-ph?style=social)](https://github.com/christiangarcia0311/data-seed-ph/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/christiangarcia0311/data-seed-ph?style=flat)](https://github.com/christiangarcia0311/data-seed-ph/issues)
![Static Badge](https://img.shields.io/badge/License-MIT-orange?style=flat)
![Static Badge](https://img.shields.io/badge/Github-data_seed_ph-green?style=flat&logo=github)
![Static Badge](https://img.shields.io/badge/Pypi-data_seed_ph-blue?style=flat&logo=pypi&logoColor=white)
![Static Badge](https://img.shields.io/badge/Python-blue?style=flat&logo=python&logoColor=white)
[![Last commit](https://img.shields.io/github/last-commit/christiangarcia0311/data-seed-ph?style=flat)](https://github.com/christiangarcia0311/data-seed-ph/commits/main)
[![Latest release](https://img.shields.io/github/v/release/christiangarcia0311/data-seed-ph?style=flat)](https://github.com/christiangarcia0311/data-seed-ph/releases/latest)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/data-seed-ph?period=total&units=NONE&style=flat&left_color=GRAY&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/data-seed-ph)


**A Python library for generating realistic, synthetic Philippine-based datasets.**

>[!NOTE]
> Designed for database seeding, API testing, machine learning dataset generation, academic research, and software development prototyping with support for CSV, JSON and SQL export formats.

#### Why Data Seed PH

Creating test data manually is time-consuming and error-prone. Data Seed PH   eliminates this burden by providing authentic Philippine data generation out of  the box perfect for developers, QA engineers, and researchers who need realistic test datasets without privacy concerns.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [CLI Feature [ New ]](#cli-feature)
- [Core Concepts](#core-concepts)
- [Features](#features)
    - [Personal Data](#1-personal-data)
    - [Address Data](#2-address-data)
    - [Contact Data](#3-contact-data)
    - [Education Data](#4-education-data)
    - [Geo Data](#5-geo-data)
- [Data Generation Types](#data-generation-types)
    - [String Keywords](#string-keywords)
    - [Numeric Ranges](#numeric-ranges-tuples)
    - [Categorical Values](#categorical-values-lists)
    - [Parameterized Keywords](#parameterized-keywords)
    - [Batch Generation [ New ]](#batch-generation)
- [Export Formats](#export-formats)
    - [CSV Export](#csv-export)
    - [JSON Export](#json-export)
    - [SQL Export](#sql-export)
        - [SQLite](#sqlite-default)
        - [MySQL / MariaDB](#mysqlmariadb)
- [Use Cases](#use-cases)
- [Important Notes](#important-notes)
- [Data Source](#data-source)
- [Releases](#releases)
- [License](#license)

### Installation 

Install via python package index [Pypi]().

```bash
pip install data-seed-ph
```

### Quick Start

Generate 1,000 rows of synthetic Philippine data with just a few lines.

```python
from seed import Dataset

# create the data instance
seed = Dataset()

# define the data structure
data = {
    'first_name': 'firstname',
    'last_name': 'lastname',
    'user_email': 'email',
    'user_mobile': 'mobile_int',
    'addr_prov': 'province',
    'addr_city': 'city'
}

# generate the data 
seed_data = seed.generate(rows=1000, features=data)

# export data to CSV, JSON or SQL
seed.save(seed_data, 'output_example', 'csv')
```

> [!NOTE]
> New added feature see [latest release](https://github.com/christiangarcia0311/data-seed-ph/releases/tag/v.3.4.9).

### CLI Feature

You can run the CLI and map generated feature data using the syntax `<column_name>:<feature_data>`.

Syntax:

- Basic: `<column_name>:<feature_data>` (example: `UserName:fullname`)
- Parameterized: `<column_name>:<feature_data>:<parameter>` (example: `Address:province:Surigao Del Norte`)

**Usage:**

Generate 100 user data.

Basic Usage:

```sh
seed generate --rows 100 --features "FirstName:firstname,LastName:lastname,UserEmail:email" --format csv --output users
```

Parameterized:

```sh
seed generate --rows 100 --features "FirstName:firstname,LastName:lastname,UserEmail:email,Address:province:Surigao Del Norte" --format csv --output users
```

### Core Concepts

**Dataset**

The main class for creating synthetic datasets, It orchestrates data providers and handles data export.

```python
from seed import Dataset

dataset = Dataset()
```

**Data Providers**

The library uses specialized providers to generate diffrent types of data:

- `PersonalDataProvider`: Filipino names, gender, birthdate, civil status, religion, blood type, etc.

- `AddressDataProvider`: Philippine regions, provinces, cities, municipalities, barangays

- `ContactDataProvider`: Philippines-format mobile numbers, email addresses

- `EducationDataProvider`: SHS strands and college courses

These are automatically initialized when you create a `Dataset` instance.

## Features

### **1. Personal Data**

Generate Filipino personal information with various options.

| Keyword | Description | Example Output |
| :--- | :---: | :---: | 
| `firstname` | Filipino first name (random gender) | "Christian" |
| `malename` | Male first name | "Archie" |
| `femalename` | Female first name | "Karen" |
| `lastname` | Filipino surname | "Garcia" |
| `suffixname` | Name suffix | "Jr.", "Sr.", "III" |
| `fullname` | Complete name with first, last, and optional suffix | "Christian Garcia Jr." |
| `gender` | Gender assignment | "male", "female" |
| `birthdate` | Birth date in YYYY-MM-DD format | "2003-03-11" |
| `age` | Age calculated from birthdate | 24 |
| `civil` | Civil Status | "Single", "Married", "Divorced", "Widowed" |
| `religion` | Religion preference | "Roman Catholic", "Iglesia Ni Cristo" |
| `bloodtype` | Blood type | "O+", "A" |
| `nationality` | Nationality | "male", "Filipino" |

**Example**

```python
data = {
    'name': 'fullname',
    'gender': 'gender',
    'birthdate': 'birthdate',
    'age': 'age',
    'marital_status': 'civil',
    'religion': 'religion',
    'blood_type': 'bloodtype'
}

seed_data = seed.generate(rows=500, features=data)
```
### **2. Address Data**

Generate authentic Philippine-geographical and location data.

| Keyword | Description | Example Output |
| :--- | :---: | :---: | 
| `region` | Philippine region (random island group) | "Region III (CALABARZON)" |
| `luzon` | Region from Luzon island group | "Region I (Ilocos Region)" |
| `visayas` | Region from Visayas island group | "Region VI (Western Visayas)" |
| `mindanao` | Region from Mindanao island group | "Region X (Northern Mindanao)" |
| `province` | Philippine province (random) | "Surigao Del Norte" |
| `province:<name>` | Province by specific name | "Surigao Del Norte", "Surigao Del Sur" |
| `city` | City or chartered city | "City of Surigao" |
| `city:<name>` | City within specific province | "City of Surigao" |
| `municipality` | Municipality | "Placer", "Tubod" |
| `municipality:name` | Municipality within specific province | "Mainit", "Sison" |
| `barangay` | Barangay (smallest administrative unit) | "San Isidro", "Trinidad" |
| `fulladdress` | Complete address (barangay, city/municipality, province, region) | "Trinidad, Surigao City, Surigao Del Norte, CARAGA" |

**Example with specific Province**

```python
data = {
    'region': 'region',
    'province': 'province:Surigao Del Norte',
    'city': 'city',
    'barangay': 'barangay'
}

seed_data = seed.generate(rows=500, features=data)
```

### **3. Contact Data**

Generate Philippine-format contact information.

| Keyword | Description | Example Output |
| :--- | :---: | :---: | 
| `mobile` | Philippine mobile number (09XXX format) | "09123456789" |
| `mobile_int` | International format mobile number | "+639123456789" |
| `email` | Email address (auto-generated from available names) | "christian.garcia@gmail.com" |

**Example**

```python
data = {
    'name': 'fullname',
    'email': 'email',
    'mobile_local': 'mobile',
    'mobile_intl': 'mobile_int'
}

seed_data = seed.generate(rows=500, features=data)
```

### **4. Education Data**

Generate education-related data aligned with Philippines standards.

| Keyword | Description | Example Output |
| :--- | :---: | :---: | 
| `strand` | Senior High School strand | "Science Technology Engineering Mathematics"  |
| `course` | College course/degree program | "BS in Computer Science", "BS in Civil Engineering" |

**Example**

```python
data = {
    'student_name': 'fullname',
    'shs_strand': 'strand',
    'college_course': 'course',
    'email': 'email'
}

seed_data = seed.generate(rows=500, features=data)
```

> [!Note]
> New feature added - Geo Data coordinates for location-based applications.

### **5. Geo Data**

Generate Philippine geographical coordinates for mapping and location-based applications.

| Keyword | Description | Example Output |
| :--- | :---: | :---: | 
| `latitude` | Random latitude within Philippines (random region) | 15.487045 |
| `longitude` | Random longitude within Philippines (random region) | 120.974123 |
| `coordinates` | Complete coordinates object with lat, long, and region | `{'latitude': 15.487045, 'longitude': 120.974123, 'region': 'Luzon'}` |
| `latitude:luzon` | Latitude within Luzon region | 15.487045 |
| `latitude:visayas` | Latitude within Visayas region | 10.812345 |
| `latitude:mindanao` | Latitude within Mindanao region | 8.234567 |
| `longitude:luzon` | Longitude within Luzon region | 120.974123 |
| `longitude:visayas` | Longitude within Visayas region | 123.456789 |
| `longitude:mindanao` | Longitude within Mindanao region | 125.123456 |

**Example**

```python
data = {
    'latitude': 'latitude',
    'longitude': 'longitude'
}

seed_data = seed.generate(rows=500, features=data)
```

## Data Generation Types

#### String Keywords

Reference built-in data generation using string keywords:

```python
data = {
    'first_name': 'firstname',
    'last_name': 'lastname',
    'email': 'email',
    'mobile': 'mobile_int',
    'province': 'province'
}
```

#### Numeric Ranges (Tuples)

Generate random integers or floats within a range:

```python
data = {
    'score': (0, 100),             
    'gpa': (2.0, 4.0, 'float'), 
    'user_id': (1000, 9999),
    'price': (99.99, 9999.99, 'float')
}
```

#### Categorical Values (Lists)

Choose randomly from predefined options:

```python
data = {
    'status': ['active', 'inactive', 'pending'],
    'priority': ['low', 'medium', 'high', 'critical'],
    'category': ['A', 'B', 'C'],
    'department': ['Sales', 'IT', 'HR', 'Finance']
}
```

#### Parameterized Keywords

Some generators acccept parameters using colon syntax:

```python
data = {
    'addr_province': 'province:Surigao Del Norte',         
    'addr_municipality': 'municipality:Claver',
    'addr_barangay': 'barangay'  
}
```

> [!Note]
> New feature added.

## Batch Generation

Generate multiple datasets with different configurations in a single operation. 

### Usage

Use `generate_batch()` to create multiple datasets at once:

```python
from seed import Dataset

# create the data instance
seed = Dataset()

# define multiple dataset configurations
configs = [
    {
        'name': 'customers',
        'rows': 1000,
        'features': {
            'customer_id': (1111, 9999),
            'full_name': 'fullname',
            'email': 'email',
            'mobile': 'mobile_int'
        }
    },
    {
        'name': 'orders',
        'rows': 1000,
        'features': {
            'order_id': (000, 999),
            'customer_id': (1111, 9999), 
            'amount': (10000, 9000, 'float')
        }
    }
]

datasets = seed.generate_batch(configs)
```

### Configuration Format

Each configuration in the list must be a dictionary with:

| Parameter | Type | Required | Description |
| :---: | :---: | :---: | :---: |
| `name` | str | No | Identifier for the batch (defaults to `batch_1`, etc.) |
| `rows` | int | Yes | Number of rows to generate (must be positive integer) |
| `features` | dict | Yes | Feature definitions using any valid data generation types | 


### Export Batch Results

use `save_batch()` to export all generated datasets with a single call:

```python
# Save all batch to CSV
seed.save_batch(datasets, format='csv', output_dir='./seed_data_csv')

# Save all batch to JSON
seed.save_batch(datasets, format='json', output_dir='./seed_data_json')

# Save all batch to SQL (sqlite)
seed.save_batch(
    datasets, 
    format='sql', 
    output_dir='./seed_data_sql',
    database_type='sqlite',
    database_name='bul_data.db'
)
```

The `save_batch()` method supports all export formats and automatically creates the output directory if needed.

## Export Formats

### **CSV Export**

Save data as comma-separated values file for spreadsheets and data analysis:

```python
seed_data = seed.generate(rows=1000, features=data)
seed.save(seed_data, 'output_example', 'csv')
```

### **JSON Export**

Save data in JSON format for APIs and web applications:

```python
seed_data = seed.generate(rows=1000, features=data)
seed.save(seed_data, 'output_example', 'json')
```

### **SQL Export**

#### SQLite (Default)

Create SQLite database files:

```python
seed_data = seed.generate(rows=1000, features=data)
seed.save(
    seed_data, 
    format='sql',
    table_name='users',
    database_type='sqlite',
    database_name='seed_data.db',
    if_exist='replace',
    primary_key='id',
    indexes=False
)
```

#### MySQL/MariaDB

Insert data into remote MySQL databases:

```python
seed_data = seed.generate(rows=1000, features=data)
seed.save(
    seed_data, 
    format='sql',
    table_name='users',
    database_type='mysql',
    database_name='seed_data',
    username='mysql_username',
    password='mysql_password',
    host='localhost',
    port=3306,
    if_exist='replace',
    primary_key='id',
    indexes=True
)
```

#### Use Cases

- **Database Seeding**: Quickly populate development and staging databases with realistic test data

- **API Testing**: Generate test payloads and bulk request data for API endpoint testing

- **Load Testing**: Create large synthetic datasets for performance and stress testing

- **Machine Learning**: Generate diverse training datasets while protecting real user privacy

- **Academic Research**: Create realistic datasets for educational data science and research projects

- **Software Prototyping**: Speed up development with pre-populated data

- **Demo Applications**: Build convincing demos with realistic Philippine data

- **Data Privacy**:  Use synthetic data to avoid GDPR/Privacy Act violations during testing

#### Important Notes

> [!IMPORTANT]
> **Synthetic Data Disclaimer**: All generated data is random and synthetic. It does NOT represent real individuals, real addresses, or real contact information. Use this library only for development, testing, research, and educational purposes.

> [!TIP]
> **Data Authenticity**: While synthetic, the data structure follows authentic Philippine geographical divisions, naming conventions, and formatting standards.


### Data Source

- [Forebears.io - forenames](https://forebears.io/philippines/forenames)

- [Forebears.io - surnames](https://forebears.io/philippines/surnames)

- [PSGC API](https://psgc.cloud/api-docs/v2) 

### Releases

[See releases](https://github.com/christiangarcia0311/data-seed-ph/releases)

### License

MIT License - See [LICENSE](/LICENSE) file for details.


### Author

[<img src="https://github.com/christiangarcia0311.png" width="80px;" style="border-radius: 100%;">](https://github.com/christiangarcia0311)