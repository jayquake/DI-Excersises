import json

def create_database(dst_file='my_file.json'):
    data = [
        {
            'name': 'iphone 9',
            'price': 799,
            'remains': True
        },

        {
            'name': 'Macbook Pro',
            'price': 4799,
            'remains': False
        },

        {
            'name': 'Apple Watch',
            'price': 10799,
            'remains': True
        },

        {
            'name': 'Apple stand pro',
            'price': 99999,
            'remains': True
        },
    ]
    with open(dst_file, 'w') as f :
        json.dump(data, f)

def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data