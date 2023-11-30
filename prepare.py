#standard ds imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#datetime utilities
from datetime import timedelta, datetime

#custom imports
import acquire

def convert_to_datetime(df):
    '''
    This function takes in a dataframe
    and converts the sales_date column to a datetime
    '''
    df.sale_date = pd.to_datetime(df.sale_date, infer_datetime_format=True)
    return df

def plot_distributions(df):
    for col in list(df.columns.drop('Date')):
        plt.figure()
        sns.histplot(df[col])
        plt.title('Distribution of {}'.format(col))