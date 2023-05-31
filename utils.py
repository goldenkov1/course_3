import datetime
import json


def load_json():
    with open("operations.json", 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def filter_executed(file):

    executed_list = []
    for i in file:
        if 'from' in i:
            if i['state'] == 'EXECUTED':
                executed_list.append(i)
    return executed_list


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda i: i['date'], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    formatted_data = []
    for row in data:
        date = datetime.datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']
        recipient = f"{row['to'].split()[0]} **{row['to'][-4]}"
        operations_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        if "from" in row:
            sender = row["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4]}"
            from_info = " ".join(sender)
        else:
            from_info, from_bill = "", ""
        formatted_data.append(f"""\
{date} {description}
{from_info} {from_bill} -> {recipient}
{operations_amount}""")
    return formatted_data
