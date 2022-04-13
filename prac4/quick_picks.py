import random


def main():
    num_picks = int(input("how many quick picks?"))
    for i in range(1,num_picks+1):
        num_list = random_num(num_picks)
        print("")




def random_num(num):
    num_list=[]
    for j in range(1, 7):
        num_list.append(random.randint(1, 45))
    num_list.sort()
    for i in range(1,7):
        print(num_list[i-1],end=" ")


main()
