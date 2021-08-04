# RFR Deployment
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "uu5F17zBZUwQbUxxqbnKBcp2gXt3tJXPxfaEOpgDUTL4"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["year","month","day"]], "values": [[1997,1,7]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/efde5787-7fe6-44ed-b6ae-7602c8004740/predictions?version=2021-08-03', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
prediction=response_scoring.json()
print(prediction['predictions'][0]['values'][0][0])