from .payload_contact import check_if_exist


def check_and_get(data):
    if data:
        if data[0] == '@' and len(data) >= 6:
            """ the data is entity, check for nodes"""
            data_contact = check_if_exist(data)
            print(data_contact)
            print(" the data is entity, check for nodes")
        else:
            if data[0] != '.' and len(data) >= 5:
                print(data.find("@"))
                if data.find("@") != -1 and data.find(".") != 1 and data.find("#") == -1:
                    """ the data is email get account """
                    # data_contact = chek_for_email
                    print(" the data is email get account ")
                elif data.find("@") == -1 and data.find(".") == -1:
                    """ the data is account name but without "." """
                    # atach "." and data_contact = get_account
                    print(" the data is account name but without ")
                else:
                    print(" the data is not correct")
                    data_contact = False

            elif data.find("@") == -1 and len(data) >= 6:
                # data_contact = get_account
                print(" the data is account name ")
            else:
                print(" the data is not correct ")
                data_contact = False
    else:
        print("the data is enty")