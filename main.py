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