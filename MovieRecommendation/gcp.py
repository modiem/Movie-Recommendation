import os
import json
import joblib
import pandas as pd

from google.cloud import storage
from google.oauth2 import service_account
from MovieRecommendation.params import PROJECT_ID, BUCKET_NAME



def get_credentials():  
    credentials_raw = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if ".json" in credentials_raw:
        credentials_raw = open(credentials_raw).read()
    creds_json = json.loads(credentials_raw)
    greds_gcp = service_account.Credentials.from_service_account_info(creds_json)
    return greds_gcp

def get_matrix(k):
    filename = f"{k}_latent_matrix.joblib"
    if os.path.exists(f"{filename}"):
        print("matrix exists.")
    else:
        creds = get_credentials()
        client = storage.Client(credentials=creds, project=PROJECT_ID).bucket(BUCKET_NAME)   
        storage_location = f"matrices/{filename}"
        blob = client.blob(storage_location)
        blob.download_to_filename(f"{filename}")
        print(f"{k} matrix saved.")
    matrix=joblib.load(f"{filename}")
    return matrix

def clean_matrix():
    for f in os.listdir():
        if f.endswith(".joblib"):
            os.remove(f) 
            print(f"{f} removed.")