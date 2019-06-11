# Clean some data
import pandas as pd
import os
import datetime as dt

env = os.getattr("RUNTIME")

if env == 'local':
    # amex
    df_amex = pd.read_csv("gdrive/My Drive/Colab_Notebooks/AmexNew2019-5.csv", header=None, usecols=[0,7])
    # chase
    df_chase = pd.read_csv('/content/gdrive/My Drive/Colab_Notebooks/chase_new.CSV', error_bad_lines=False)
    # amazon
    df_amazon = pd.read_csv('/content/gdrive/My Drive/Colab_Notebooks/Amazon.csv')
    
if env == 'gcp_function':
    # TODO
    raise Exception("Data Cleansing not implement for GCP")
    


    
