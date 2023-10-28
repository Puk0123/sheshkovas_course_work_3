from develop import utils

def test_get_data():
    assert len(utils.get_data("operations.json")[0]) > 0

def test_get_operations_executed(test_data):
    assert len(utils.get_operations_executed(test_data)) == 2

def test_get_last_num_operations(test_data):
    assert len(utils.get_last_num_operations(test_data, 4)) == 4
    assert utils.get_last_num_operations(test_data, 4)[0]['date'] == '2023-07-03T18:35:29.512364'

def test_get_operations_formatted(test_data):
    assert utils.get_operations_formatted(test_data)  == ['\n'
 '            26.08.2019 Перевод организации\n'
 '            Maestro 1596 83** **** 5199->Счет **9589\n'
 '            31957.58 руб. ',
 '\n'
 '            03.07.2023 Перевод организации\n'
 '            MasterCard 7158 30** **** 6758->Счет **5560\n'
 '            8221.37 USD ',
 '\n'
 '            30.06.2018 Перевод организации\n'
 '            Счет **6952->Счет **6702\n'
 '            9824.07 USD ',
 '\n'
 '            23.03.2018 Открытие вклада\n'
 '             **6952->Счет **2431\n'
 '            48223.05 руб. ']