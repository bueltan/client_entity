from gql import gql, Client, AIOHTTPTransport
from connection_endpoint import base_url_http
transport = AIOHTTPTransport(url=base_url_http)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

def sentMessage(**kwargs):
    string_query = """
            mutation { CreateMessage
                           (messageData:{*type: $type *text: $text *fromMe: $fromMe *mime: $mime 
                                         *url: $url *caption: $caption *filename: $filename *payload: $payload 
                                         *vcardList: $vcardList }
                           ticketData:{*id: $id *idTk: $idTk *idCode: $idCode *node2: $node2 
                                       *node3: $node3 *node4: $node4 *phone: $phone }
                           idAccount:{id: $userId })
                           {message{id}} }
                     """

    variables = {'type': None, 'text': None, 'fromMe': None,
                 'mime': None, 'url': None, 'caption': None,
                 'filename': None, 'payload': None, 'vcardList': None,
                 'id': None, 'idTk': None, 'idCode': None,
                 'node2': None, 'node3': None, 'node4': None,
                 'phone': None, 'userId': None}

    for key in kwargs:
        variables[key] = kwargs.get(key)


    for key in variables:
        if variables[key] != None:
            old_str = ': ' + "$" + str(key) + ' '
            if type(variables[key]) == str:
                new_str = ': "' + str(variables[key]) + '" '
            else:
                new_str = ': ' + str(variables[key]) + ' '
            string_query = string_query.replace(old_str, new_str)
            string_query = string_query.replace('*' + key, key)
        else:
            pop_var = '*' + key + ': $' + key + ' '
            string_query = string_query.replace(pop_var, '')

    query = gql(string_query)
    result = client.execute(query)
    return result