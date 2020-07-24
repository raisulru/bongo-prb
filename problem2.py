import inspect

class Person(object):
    
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)

data = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': person_b
        }
    }
}

def print_depth(data, depth=1):
    if data:
        nested_data = None
        if isinstance(data, Person):
            data = data.__dict__
        for key, value in data.items():
            if isinstance(value, dict) or isinstance(value, Person):
                nested_data = value
            print(key, depth)
        depth+=1
        return print_depth(nested_data, depth)
    return 0

print_depth(data=data)
