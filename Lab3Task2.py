import json

def reading(path):
    '''
    The function reads a json file and converts the information into
    dictionary
    '''
    file_1 = open(path, encoding = "utf-8")
    data = json.load(file_1)
    return data

def inception(dictionary):
    '''
    The function propese user to choose which object he would like
    to look at. IF a user sees dictionary he is able to choose a key,
    if he sees a list he is able to choose an elemnt with a pecific
    index. The program continues working until the user sees an object
    which is neither a dict nor list.
    '''

    if isinstance(dictionary,dict):

        print("An object type is dictionary.\
             Please enter the key you are interested in to move futher: \n",list(dictionary.keys()))
        choice = input()

    elif isinstance(dictionary,list):
        if len(dictionary)>0:
            print(dictionary)
            index = int(input("An object type is list. Please enter the index of elment you are interesetd in \n"))
        else:
            return "empty"

        if isinstance(dictionary[index],dict):
            return inception(dictionary[index])

        elif not isinstance(dictionary,dict) and not isinstance(dictionary,list):
                return dictionary[choice] 
        else:

            return dictionary[index]
    else:

        return dictionary
    return inception(dictionary[choice])
