import pytest

from utils import load_json, filter_executed, get_last_values, get_formatted_data


@pytest.fixture()
def test_data():
    return load_json()


def test_load_json():
    data = load_json()
    assert isinstance(data, list)


def test_filter_executed(test_data):
    assert filter_executed(test_data[:2]) == [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }]


def test_get_last_values(test_data):
    data = get_last_values(filter_executed(test_data), 5)
    assert [i['date'] for i in data] == ['2019-12-07T06:17:14.634890', '2019-11-19T09:22:25.899614',
                                         '2019-11-13T17:38:04.800051', '2019-10-30T01:49:52.939296',
                                         '2019-09-29T14:25:28.588059']


def test_get_formatted_data(test_data):
    data = get_formatted_data(get_last_values(filter_executed(test_data), 5))
    assert data == ['07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9 -> Счет **3\n48150.39 USD',
                    '19.11.2019 Перевод организации\nMaestro 7810 84** **** 5 -> Счет **2\n30153.72 руб.',
                    '13.11.2019 Перевод со счета на счет\nСчет 3861 14** **** 9 -> Счет **8\n62814.53 руб.',
                    '30.10.2019 Перевод с карты на счет\nVisa Gold 7756 67** **** 2 -> Счет **9\n23036.03 руб.',
                    '29.09.2019 Перевод со счета на счет\nСчет 3542 14** **** 9 -> Счет **4\n45849.53 USD']
