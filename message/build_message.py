from querries.sent_message import sentMessage


class build_message():
    def __init__(self, ):
        super(build_message, self).__init__()

    @staticmethod
    def exec_query(payload):
        payload['idCode'] = payload.pop('id_code')
        print(" in staticmethod ",type(payload), payload)
        sentMessage(**payload)
