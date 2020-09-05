from gql import gql, Client, AIOHTTPTransport
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(process)d-%(levelname)s-%(message)s-%(thread)d')
# Select your transport with a defined url endpoint


transport = AIOHTTPTransport(url="http://localhost:5000/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=False)

# Provide a GraphQL query
query = gql(
    """
  mutation ($node4:String!){CreateMessage  (
  messageData:{type:"text" text:$node4}
  ticketData:{idTk:"QWNjb3VudDoy" node4:".denis"}
  idAccount:{id:"QWNjb3VudDoy"}){message{id}}}
"""
)

# Execute the query on the transport
logging.debug(msg="start")
variables = {'node4':".sergio"}
result = client.execute(query,variable_values=variables)
logging.debug(msg="end")

print(result)