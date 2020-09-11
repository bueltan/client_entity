from graphql_client import GraphQLClient

ws = GraphQLClient('ws://192.168.0.11:5000/subscriptions')


def callback(_id, data):
    print(data)


query = """
subscription($id_code: String!, $node_2: String!, $node_3: String!, $node_4: String!){getTK(
  idCode:$id_code 
  node2:$node_2
  node3:$node_3
  node4:$node_4
)} 
"""

variables = {'id_code': "4640", 'node_2': "@Cyberlink", 'node_3': "#ventas", 'node_4': ""}

sub_id = ws.subscribe(query, variables=variables, callback=callback)

# later stop the subscription
# ws.stop_subscribe(sub_id)
# ws.close()
