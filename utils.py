import json
from datetime import datetime
import os

print(os.getcwd())

def get_data(filename):
    with open(filename, 'r') as file:
        data: object = json.load(file)
        return data
