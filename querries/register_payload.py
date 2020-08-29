from Connection_endpoint import send_payload


def get_id(value, resolve, field):
    payload = '{"query": "{' + resolve + ' (' + field + ':\\"' + value + '\\"){id}}"}'
    json = send_payload(payload)
    print(payload)
    if json is not None:
        if json['data'][resolve] is not None:
            id = (json['data'][resolve]['id'])
            return id
        else:
            id = None
            return id


def create_account(name, password, email):
    payload = '{"query": "mutation{createAccount(input:{idName:\\"' + name + '\\",password:\\"' + password + '\\",email:\\"' + email + '\\"}){account{id}}}"}'
    json = send_payload(payload)
    print(payload)
    if json is not None:
        id = (json['data']['createAccount']['account']['id'])

    return id
