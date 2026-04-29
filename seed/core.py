'''
Core Module 

This module is responsible for generating synthetic datasets using
different data providers such as personal information, address data,
contact details and education information. It acts as the core interface for assembling mock
datasets and exporting them into different formats.

The dataset generator allows developers to define:
    - number of rows to generate
    - data features/fields to include 
    - output format (CSV, JSON, SQL)

Notes
-----
All generated data is synthetic and intended strictly for development,
testing, research, and educational purposes.

Information
-----------
@author: Christian Garcia
@github: github.com/christiangarcia0311/data-seed-ph
'''


from .exports.exporter import SaveData
from .providers.data_provider import (
    PersonalDataProvider,
    AddressDataProvider,
    ContactDataProvider,
    EducationDataProvider,
    GeoDataProvider
)

import pandas as pd
import numpy as np
import random as rd
import os

    

class Data:
    
    def __init__(self):
        self.personal = PersonalDataProvider()
        self.address = AddressDataProvider()
        self.contact = ContactDataProvider(self.personal)
        self.education = EducationDataProvider()
        self.geo = GeoDataProvider()

class Dataset:
    
    def __init__(self):
        self.export = SaveData()
        self.data = Data()
        self.dump = {}
        
        self.data_map = {
            # Personal data
            'firstname': lambda: self.data.personal.firstname(),
            'lastname': lambda: self.data.personal.lastname(),
            'suffixname': lambda: self.data.personal.suffix(),
            'fullname': lambda: self.data.personal.fullname(),
            'malename': lambda: self.data.personal.firstname(gender='male'),
            'femalename': lambda: self.data.personal.firstname(gender='female'),
            'gender': lambda: self.data.personal.gender(),
            'birthdate': lambda: self.data.personal.birthdate(),
            'age': lambda: self.data.personal.age(),
            'civil': lambda: self.data.personal.civil(),
            'religion': lambda: self.data.personal.religion(),
            'bloodtype': lambda: self.data.personal.blood_type(),
            'nationality': lambda: self.data.personal.nationality(),
            
            # Address data
            'region': lambda: self.data.address.region(),
            'luzon': lambda: self.data.address.region('luzon'),
            'visayas': lambda: self.data.address.region('visayas'),
            'mindanao': lambda: self.data.address.region('mindanao'),
            'province': lambda: self.data.address.province(),
            'city': lambda: self.data.address.city(),
            'municipality': lambda: self.data.address.municipality(),
            'barangay': lambda: self.data.address.barangay(),
            'fulladdress': lambda: self.data.address.full_address(),
            
            # Contact data
            'mobile': lambda: self.data.contact.mobile(),
            'mobile_int': lambda: self.data.contact.mobile('international'),
            'email': lambda: self.data.contact.email(),
            
            # Education data
            'course': lambda: self.data.education.course(),
            'strand': lambda: self.data.education.strand(),
            
            # Geo data
            'latitude': lambda: self.data.geo.coordinates()['latitude'],
            'longitude': lambda: self.data.geo.coordinates()['longitude'],
            'coordinates': lambda: self.data.geo.coordinates(),
            'latitude:luzon': lambda: self.data.geo.coordinates('Luzon')['latitude'],
            'latitude:visayas': lambda: self.data.geo.coordinates('Visayas')['latitude'],
            'latitude:mindanao': lambda: self.data.geo.coordinates('Mindanao')['latitude'],
            'longitude:luzon': lambda: self.data.geo.coordinates('Luzon')['longitude'],
            'longitude:visayas': lambda: self.data.geo.coordinates('Visayas')['longitude'],
            'longitude:mindanao': lambda: self.data.geo.coordinates('Mindanao')['longitude'],
        }
        
    def _reset_providers(self):
        self.data.personal = PersonalDataProvider()
        self.data.address = AddressDataProvider()
        self.data.contact = ContactDataProvider(self.data.personal)
        self.data.education = EducationDataProvider()
        self.data.geo = GeoDataProvider()
    def generate(self, rows: int, features: dict) -> pd.DataFrame:
        self.dump = {feature: [] for feature in features}

        for _ in range(rows):
            for feature, value in features.items():
                if isinstance(value, str):
                    key = value.lower()
                    
                    if ':' in key:
                        keyword, param = value.split(':', 1)
                        keyword = keyword.strip().lower()
                        param = param.strip()

                        if keyword == 'province':
                            self.dump[feature].append(self.data.address.province(param))
                        elif keyword == 'city':
                            self.dump[feature].append(self.data.address.city(param))
                        elif keyword == 'municipality':
                            self.dump[feature].append(self.data.address.municipality(param))
                        elif keyword == 'latitude':
                            coords = self.data.geo.coordinates(param)
                            self.dump[feature].append(coords['latitude'])
                        elif keyword == 'longitude':
                            coords = self.data.geo.coordinates(param)
                            self.dump[feature].append(coords['longitude'])
                        else:
                            raise ValueError(f'Unknown parameterized keyword: {keyword}')

                    elif key in self.data_map:
                        self.dump[feature].append(self.data_map[key]())
                    
                    else:
                        raise ValueError(f'Unknown feature keyword: {value}')

                elif isinstance(value, tuple):
                    min_value, max_value = value[0], value[1]
                    if len(value) == 3 and value[2] == 'float':
                        self.dump[feature].append(round(float(np.random.uniform(min_value, max_value)), 2))
                    else:
                        self.dump[feature].append(int(np.random.randint(min_value, max_value + 1)))

                elif isinstance(value, list):
                    self.dump[feature].append(rd.choice(value))

                else:
                    raise ValueError('Feature values must be a tuple for numerical ranges or a list for categorical values.')

        return pd.DataFrame(self.dump)
    
    '''
    v.3.4.2: [feat #1] Batch Generation with Variations
    ----------------------------------------------------
    '''
    
    def generate_batch(self, configurations: list) -> dict:
        batch_results: dict = {}
        
        for index, config in enumerate(configurations):
            
            if not isinstance(config, dict): raise ValueError(f'Configuration at index {index} must be a dictionary format.')
            if 'rows' not in config or 'features' not in config: raise ValueError(f'Configuration at index {index} must contain `features` keys and `rows`')
            
            batch_name = config.get('name', f'batch_{index + 1}')
            
            rows = config['rows']
            features = config['features']  
            
            if not isinstance(rows, int) or rows <= 0: raise ValueError(f'Batch {batch_name} must be a postive integer.')
            if not isinstance(features, dict) or not features: raise ValueError(f'Batch {batch_name}: features cannot be empty dictionary.')
            
            self._reset_providers()
            
            batch_results[batch_name] = self.generate(rows=rows, features=features)
            
        return batch_results
    
    def save(
        self, 
        data: dict, 
        filename: str, 
        format: str, 
        table_name: str = 'seeds',
        database_type: str = 'sqlite',
        database_name: str = 'data_seed.db',
        username: str = None, 
        password: str = None,
        host: str = 'localhost',
        port: int = None,
        if_exist: str = 'fail',
        primary_key: str = 'id',
        indexes: bool = False
    ):
        match (format.lower()):
            case 'csv':
                self.export.to_csv(data=data, filename=f'{filename}.{format}')
            case 'json':
                self.export.to_json(data=data, filename=f'{filename}.{format}')
            case 'sql':
                if database_type.lower() == 'sqlite':
                    self.export.to_sql(
                        data=data,
                        table_name=table_name,
                        database_type=database_type,
                        database_name=database_name,
                        if_exist=if_exist,
                        primary_key=primary_key,
                        indexes=indexes
                    )
                elif database_type.lower() == 'mysql':
                    self.export.to_sql(
                        data=data,
                        table_name=table_name,
                        database_type=database_type,
                        database_name=database_name,
                        username=username,
                        password=password,
                        host=host,
                        port=port,
                        if_exist=if_exist,
                        primary_key=primary_key,
                        indexes=indexes
                    )
                else:
                    raise ValueError(f'Unsupported database type: {database_type}')
            case _:
                raise ValueError(f'Unsupported format: {format}')
    
    def save_batch(
        self, 
        batch_data: dict, 
        format: str, 
        output_dir: str = './output', 
        **kwargs
    ):
        os.makedirs(output_dir, exist_ok=True)
        
        for batch_name, data in batch_data.items():
            filename = os.path.join(output_dir, batch_name)
            
            try:
                self.save(
                    data=data,
                    filename=filename,
                    format=format,
                    **kwargs
                )
                
                print(f'Batch {batch_name} successfully saved.')
            except Exception as e:
                print(f'Error saving batch {batch_name}: {e}')
