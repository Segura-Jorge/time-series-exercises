import requests
import pandas as pd

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