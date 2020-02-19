import json

def create_database(dst_file='my_file.json'):
    data = [
        {
            'username': 'Jason',
            'password': 'horse',
            'status': True
        },

        {
            'username': 'Mac',
            'password': 'candy' ,
            'status': False
        },

        {
            'username': 'Apple',
            'password': 'monkeydog',
            'status': True
        },

    ]
    with open(dst_file, 'w') as f :
        json.dump(data, f)

def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data

def write_database(src_file='my_file.json'):
    with open(src_file, 'w') as f:
        json.dump(f)
    return ('database rewritten')