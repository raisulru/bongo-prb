data = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4
        }
    }
}

def print_depth(dictionary, depth=1):
    if isinstance(dictionary, dict):
        for item in dictionary.keys():
            print(item, depth)
        depth+=1
        return print_depth(dictionary[max(dictionary)], depth)
    return 0
print_depth(dictionary=data)