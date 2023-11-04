import re


def task_1():
    # "a": True, "b": False, "c": True

    dauletsuper = input("Input: ")
    user_input = re.sub(r'[.,!?:"]', '', dauletsuper).split()

    my_dict = {}

    def get_keys_with_value_true(word_list):
        i = 0
        while i < len(word_list) - 1:
            if word_list[i + 1].lower() == "true":
                my_dict[word_list[i]] = True
                i += 2
            else:
                my_dict[word_list[i]] = False
                i += 2
        return my_dict

    my_dict = get_keys_with_value_true(user_input)

    for key, value in my_dict.items():
        if value:
            print(key)


# task_1()

def task_2():
    # user input: 1, 2, 3, 1, 2, 4
    user_input = input("Input: ")
    user_input = re.sub(r'[.,!?:"#]', '', user_input).split()
    lists, element = [int(x) for x in user_input], []

    def get_unique_elements(list):
        min_element_list = {}
        for x in list:
            count = list.count(x)
            if (x, count) not in min_element_list:
                min_element_list[x] = count
        return min_element_list

    min_element_list = get_unique_elements(lists)
    min_value = min(min_element_list.values())
    print_elements = [k for k, v in min_element_list.items() if v == min_value]

    print(print_elements)


# task_2()

def task_3():
    user_input = str(input("Date: ")).split('.')
    lists = []
    for date in user_input:
        lists.append(date)

    text = '.'.join(lists[::-1])
    print(text)


# task_3()

def task_4():
    user_input = input("Input: ")
    user_input = re.sub(r'[.,!?:"#]', '', user_input).split()

    lists = set(int(x) for x in user_input)

    print_list = []
    print_list = sorted(lists)

    first_element, second_element = print_list[0], print_list[1]

    print(first_element, second_element)


# task_4()

def task_5():
    user_input = input("Input: ")
    user_input = re.sub(r'[,!?:"#]', '', user_input).split()
    lists = [str(x) for x in user_input]

    print(lists)


# task_5()

def task2_6():
    user_input = input("Input: ")
    user_input = re.sub(r'[.,!?:"#]', '', user_input).split()
    lists = [int(x) for x in user_input]

    def get_unique_elements(list):
        min_element_list = {}
        for x in list:
            count = list.count(x)
            if (x, count) not in min_element_list:
                min_element_list[x] = count
        return min_element_list

    print(get_unique_elements(lists))


# task2_6()

def task2_7():
    user_input = int(input("Number: "))

    def prime_number(number):
        for x in range(2, number + 1):
            if x == number:
                return True
            if number % x == 0:
                return False
        return True

    i = 5
    lists = [2, 3]

    while i < user_input:
        if prime_number(i):
            lists.append(i)
        i += 2
    print(lists)


# task2_7()

def task2_8():
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99
    def prime_number(number):
        for x in range(2, number + 1):
            if x == number:
                return True
            if number % x == 0:
                return False
        return True

    user_input = input("List: ").split(', ')
    lists = [int(x) for x in user_input]
    prime_number_list = []
    i = 0

    while i < len(lists):
        if prime_number(lists[i]):
            prime_number_list.append(lists[i])
        i += 1

    print(prime_number_list)


# task2_8()

def task2_9():
    from datetime import date

    user_input_first = input("First date: ").split(".")
    user_input_second = input("Second date: ").split(".")

    first_time_list = [int(x) for x in user_input_first]
    second_time_list = [int(x) for x in user_input_second]

    first_date = date(first_time_list[0], first_time_list[1], first_time_list[2])
    second_date = date(second_time_list[0], second_time_list[1], second_time_list[2])

    result = abs(first_date - second_date)

    print(result)


# task2_9()

def task3_10():
    user_input = input("Binary number: ")
    user_input = int(user_input, 2)
    print(user_input)


# task3_10()

def task3_11():
    import math
    user_input = input("Numbers: ").split(', ')
    lists = [int(x) for x in user_input]

    for number in lists:
        check_number = math.sqrt(number)
        if check_number == int(check_number):
            print(True, number)
        else:
            print(False, number)


# task3_11()

def task3_12():
    # {"name": "Apple", "price": 100}, {"name": "Banana", "price": 50}, {"name": "Orange", "price": 20}
    user_input = input("String: ")

    user_list = user_input.split('}, {')

    user_list[0] = user_list[0].replace('{', '')
    user_list[-1] = user_list[-1].replace('}', '')

    result_list = []
    for item in user_list:
        item = item.strip()
        item = f'{{{item}}}'
        result_list.append(eval(item))
    print(result_list)


# task3_12()


def task3_13():
    user_input = input("String: ").replace('""', '').split(', ')
    vow_lists = []

    for letter in ('aeiouy'):
        vow_lists.append(letter)

    user_list = [x for x in user_input]

    for element in user_list:
        if element[0] in vow_lists:
            print(element)


task3_13()
