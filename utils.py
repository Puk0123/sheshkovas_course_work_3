"""
Требоания:
Последние 5 выполненных (EXECUTED) операций выведены на экран.
Операции разделены пустой строкой.
Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
Сверху списка находятся самые последние операции (по дате).
Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
Номер счета замаскирован и не отображается целиком в формате  **XXXX
(видны только последние 4 цифры номера счета).
"""

import json
from datetime import datetime
import os

print(os.getcwd())

def get_data(filename):
    """
    Получает данные из operations.json
    """
    with open(filename, 'r') as file:
        data: object = json.load(file)
        return data


def get_operations_executed(data):
    """
    Проверяет статус перевода
    """
    operations_executed= []
    for operation in data:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            operations_executed.append(operation)
        operation_with_from = []
        for operation in operations_executed:
            if 'from' in operation:
                operation_with_from.append(operation)
    return operation_with_from


def get_last_num_operations(operations_with_from, num_of_operations):
    """
    Проверяет последние операции
    """
    operations_sort = sorted(operations_with_from, key=lambda operation: operation["date"], reverse=True)
    last_five_operations = operations_sort[0:num_of_operations]
    return last_five_operations


def get_operations_formatted(last_five_operations):
    """
    Форматирует последние 5 операций в соответствие с требованиями
    """
    operations_formatted_list = []
    for operation in last_five_operations:
        date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = operation['description']
        payer_info, payment_method = "", ""
        if "from" in operation:
            payer = operation["from"].split()
            payment_method = payer.pop(-1)
            if payer[0] == 'Счет':
                payment_method_from = f"**{payment_method[-4:]}"
            else:
                payment_method_from = f"{payment_method[:4]} {payment_method[4:6]}** **** {payment_method[-4:]}"
            payer_info = " ".join(payer)
        recipient = f"{operation['to'].split()[0]} **{operation['to'][-4:]}"
        operation_amount = f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
        operations_formatted_list.append(f"""
                    {date} {description}
                    {payer_info} {payment_method_from}->{recipient}
                    {operation_amount} """)
    return operations_formatted_list