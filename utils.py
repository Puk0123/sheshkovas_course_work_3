import json
from datetime import datetime
import os

print(os.getcwd())

def get_data(filename):
    with open(filename, 'r') as file:
        data: object = json.load(file)
        return data



def get_operations_executed(data):
    operations_executed= []
    for operation in data:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            operations_executed.append(operation)
        operation_with_from = []
        for operation in operations_executed:
            if 'from' in operation:
                operation_with_from.append(operation)
    return operation_with_from
