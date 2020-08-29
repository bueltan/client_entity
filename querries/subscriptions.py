import Connection_endpoint
from graphql_client import GraphQLClient
import traceback
import sys

traceback_template = '''Traceback (most recent call last):
  File "%(filename)s", line %(lineno)s, in %(name)s
%(type)s: %(message)s\n''' # Skipping the "actual line" item

class subscriptions():
    def __init__(self, mainwid, **kwargs):
        super(subscriptions, self).__init__()
        self.mainwid = mainwid

    def getTK(self, variables):
        query = """
        subscription($id_code: String!, $node_2: String!, $node_3: String!, $node_4: String!){getTK(
          idCode:$id_code 
          node2:$node_2
          node3:$node_3
          node4:$node_4
        )} 
        """
        try:
            ws = GraphQLClient(Connection_endpoint.base_url_ws)
            ws.subscribe(query, variables=variables, callback=self.mainwid.callback)
            print(variables)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()  # most recent (if any) by default

            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'lineno': exc_traceback.tb_lineno,
                'name': exc_traceback.tb_frame.f_code.co_name,
                'type': exc_type.__name__,
                'message': str(exc_value),  # or see traceback._some_str()
            }

            del (exc_type, exc_value, exc_traceback)

            print(traceback.format_exc())
            print(traceback_template % traceback_details)




