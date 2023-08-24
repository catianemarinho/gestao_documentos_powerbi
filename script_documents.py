import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

last_page = False
page = 1
documents = []

while last_page == False:
    url = f"http://sandbox.clicksign.com/api/v1/documents?page={page}&access_token={API_KEY}"
    response = requests.get(url).json()
 
    # Iterate over each document in the response and append it to the `documents` list
    for document in response["documents"]:    
        documents.append(document)
    
    # Iterate over each document in the response and append it to the `documents` list
    last_page = response["page_infos"]["last_page?"]
    
    # Increment the page number
    page += 1

# Create a list of lists with the desired values from the documents
values = [[document["key"], document["folder_id"], document["filename"], document["uploaded_at"], document["updated_at"], document["finished_at"], document["deadline_at"], document["status"], document["auto_close"]] for document in documents]

# Define the column names for the DataFrame
columns = ["key", "folder_id", "filename", "uploaded_at", "updated_at", "finished_at", "deadline_at", "status", "auto_close"]
# Create a DataFrame using the values and columns
tabela = pd.DataFrame(columns=columns, data=values)
print("Table created!")