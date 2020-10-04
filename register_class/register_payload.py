from connection_endpoint import send_payload


def to_check(value, resolve, field):
    payload = '{"query": "{' + resolve + ' (' + field + ':\\"' + value + '\\"){'+field+'}}"}'
    json = send_payload(payload)
    print(payload)
    print(json)
    if json:
        if json['data'][resolve] is not None and not False:
            id = (json['data'][resolve][field])
            return id
    if json is None:
        return None
    if json is False:
        return False

def create_account(name, password, email):
    payload = '{"query": "mutation{createAccount(input:{idName:\\"' + name + '\\",password:\\"' + password + '\\",email:\\"' + email + '\\"}){account{id}}}"}'
    json = send_payload(payload)
    if json is not None and not False:
        id = (json['data']['createAccount']['account']['id'])
        return id
    if json is None:
        return None
    if json is False:
        return False
