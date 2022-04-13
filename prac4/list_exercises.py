def get_number():
    number_list = []
    for i in range(1, 6):
        input_number = int(input("please enter No.{} number:".format(i)))
        number_list.append(input_number)
    return number_list


def main():
    user_list = get_number()
    output_list = [user_list[0], user_list[-1], min(user_list), max(user_list), sum(user_list) / len(user_list)]
    for i in range(1, 6):
        print("Number:{:2}".format(user_list[i - 1]))
    print("""The first number is {:2}
The last number is {:2}
The smallest number is {:2}
The largest number is {:2}
The average of the numbers is {:2}
    """.format(output_list[0], output_list[1], output_list[2], output_list[3], output_list[4]))


main()

2
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    name = input("please enter your name:")
    if name in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()


