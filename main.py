from utils import load_json, filter_executed, get_last_values, get_formatted_data


def main():

    data = load_json()

    data = filter_executed(data)
    data = get_last_values(data, 5)
    data = get_formatted_data(data)
    print('INFO: Вывод транзакций...')
    for row in data:
        print(row, end='\n\n')


if __name__ == "__main__":
    main()
