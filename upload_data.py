from pymongo.mongo_client import MongoClient
import pandas as pd
import json
from urllib.parse import quote_plus

# Encode username and password
username = quote_plus("vishal")
password = quote_plus("Kaizen@123")

# Construct the MongoDB URI with encoded username and password
uri = f"mongodb+srv://{username}:{password}@cluster0.bt51f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create MongoDB client
client = MongoClient(uri)

# Define database name and collection name
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

# Read CSV file into a DataFrame
df = pd.read_csv("notebooks/wafer_23012020_041211.csv")

# Drop the unnamed column if necessary
df = df.drop("Unnamed: 0", axis=1)


json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)