import requests
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(process)d-%(levelname)s-%(message)s-%(thread)d')
# Select your transport with a defined url endpoint

# Create a GraphQL client using the defined transport
server_url = 'http://localhost:5000/'
base_url = server_url + 'graphql'
base_url_ws = 'ws://localhost:5000/subscriptions'
headers = {'content-type': 'application/json'}

payload = '{"query":"{accountList {edges {node {id}}}}"}'
logging.debug(msg="start")

response = requests.post(base_url, headers=headers, data=payload)
json = response.json()
print(json)
logging.debug(msg="end")
