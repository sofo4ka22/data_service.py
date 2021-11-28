# модуль призначено для роботи з зовнішним файлом 
# читання та виведення для візуального контролю

# читання файла table1
def get_price():
    """читання файлів ' table1 '
    та формування списку ринків 
    повертає список ринків 
    """


    # накопичення даних файлу у списках
    with open("./data/table1.csv", 'r') as f:
        prices = f.readlines()

   # підготовка даних файлу у списку 
        prices_splitted = []
    # порізати в циклі строки на окремі елементи
        for price in prices:
            object = split_line(price)
            prices_splitted.append(object)

    prices_splitted
    return

def split_line(line):
    """повертає сисок обєктів з строки """
    object = line.split(',')
    return object
    
# читання файла table2
def get_group():
    """читання файлів ' table2 '
    та формування списку товарних груп
    повертає список товарних груп 
    """


    # накопичення даних файлу у списках
    with open("./data/table2.csv", 'r') as f:
        groups = f.readlines()

   # підготовка даних файлу у списку 
        groups_splitted = []
    # порізати в циклі строки на окремі елементи
        for group in groups:
            object = split_line(price)
            groups_splitted.append(object)

    groups_splitted
    return
# вивід списку цін
def show_prices(prices):
    '''виводить список клієнтів по заданому інтервалу кодів '''
    # задати інтервал кодів 
    price_code_from = int(input('З якого кода ціни?'))
    price_code_to = int(input('до якого кода ціни?'))


    # відбір списку цін
    filtered_prices = []
    for price in ptices:
        if price_code_from <= price[0] <= price_code_to:
            filtered_prices.append(price)

    if len(filtered_prices) == 0:
        print(' В  списку цін нема таких кодів')
        return

    # вивід списку
    print('СПИСОК ЦІН')
    for price in filtered_prices:
        print(f'код товарної групи : {price[0]:3} план: {price[1]:20} очікуємо виконання:{price[2]:25} рік{price[3][:-1]:30}')

   # вивід списку товарних груп
    def show_groups(groups):
    '''виводить список клієнтів по заданому інтервалу кодів'''
    # задати інтервал кодів 
    group_code_from = int(input('З якого кода товарної групи?'))
    group_code_to = int(input('до якого кода товарної групи?'))


    # відбір списку цін
    filtered_groups = []
    for group in groups:
        if group_code_from <= group[0] <= group_code_to:
            filtered_prices.append(group)

    if len(filtered_group) == 0:
        print(' В  списку цін нема таких кодів')
        return

    # вивід списку
    print('СПИСОК ЦІН')
    for group in filtered_groups:
        print(f'код товарної групи : {group[0]:3} найменування тов групи: {group[1]:20} торгова знижка: {group[2][:-1]:25}')

    if__name__ == '__main__':
    prices = get_prices()
    group = get_group()

    show_prices(prices)
    show_group(groups)

    pass
