import requests
import os
import pandas as pd
from env import username, host, password



def fetch_swapi_people(url='https://swapi.dev/api/people/'):
    people = pd.DataFrame()
    while url:
        response = requests.get(url)
        data = response.json()
        current_page = pd.DataFrame(data['results'])
        people = pd.concat([people, current_page], ignore_index=True)
        url = data['next']
    return people

def fetch_swapi_planets(url='https://swapi.dev/api/planets/'):
    planets = pd.DataFrame()
    while url:
        response = requests.get(url)
        data = response.json()
        current_page = pd.DataFrame(data['results'])
        planets = pd.concat([planets, current_page], ignore_index=True)
        url = data['next']
    return planets

def fetch_swapi_starships(url='https://swapi.dev/api/starships/'):
    starships = pd.DataFrame()
    while url:
        response = requests.get(url)
        data = response.json()
        current_page = pd.DataFrame(data['results'])
        starships = pd.concat([starships, current_page], ignore_index=True)
        url = data['next']
    return starships

import pandas as pd

def save_and_concat_dfs(df_list, file_names):
    """
    Saves each DataFrame in df_list to a CSV file with corresponding names in file_names.
    Then concatenates these DataFrames into a single DataFrame and returns it.

    :param df_list: List of DataFrames to save and concatenate
    :param file_names: List of file names for saving each DataFrame as CSV
    :return: A single concatenated DataFrame
    """
    if len(df_list) != len(file_names):
        raise ValueError("Length of df_list and file_names must be the same")

    # Save each DataFrame to its corresponding CSV file
    for df, file_name in zip(df_list, file_names):
        df.to_csv(file_name, index=False)

    # Concatenate all DataFrames
    concatenated_df = pd.concat(df_list, axis=0, ignore_index=True)

    return concatenated_df



def get_connection(db, user=username, host=host, password=password):
    
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def acquire_store():
    
    filename = 'store.csv'
    
    if os.path.exists(filename):
        
        return pd.read_csv(filename)
    
    else:
        
        query = '''
                SELECT sale_date, sale_amount,
                item_brand, item_name, item_price,
                store_address, store_zipcode
                FROM sales
                LEFT JOIN items USING(item_id)
                LEFT JOIN stores USING(store_id)
                '''
        
        url = get_connection(db='tsa_item_demand')
        
        df = pd.read_sql(query, url)
        
        df.to_csv(filename, index=False)
        
        return df
    
def get_germany_data():
    '''
    This function creates a csv of germany energy data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('opsd_germany_daily.csv'):
        df = pd.read_csv('opsd_germany_daily.csv', index_col=0)
    
    else:
        url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
        df = pd.read_csv(url)
        df.to_csv('opsd_germany_daily.csv')

    return df