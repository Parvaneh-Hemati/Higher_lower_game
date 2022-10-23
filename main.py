import art
from game_data import data
from random import randint
#print(art.vs)


def findhigher(selected_value, value):
    if selected_value > value:
        return 1
    else:
        return 0


#read detaiol informatiom from data list


def game(i):
    print(art.logo)
    str_des = "A) "
    str_comp = "B) "
    for people in data[i]:
        str_des = str_des + " " + people + ": " + str(data[i][people]) + ", "
        if people == "follower_count":
            value_B = data[i + 1][people]
        else:
            str_comp = str_comp + " " + people + ": " + str(
                data[i + 1][people]) + ", "
    value_A = data[i]["follower_count"]
    print(str_des)
    print(art.vs)
    print(str_comp)

    print("***********************************")

    select_value = input("Select A vS B : ")
    if select_value == "A":
        win = findhigher(value_A, value_B)
    else:
        win = findhigher(value_B, value_A)
    if win:
        print("win --------------------")
        game(i + 1)
    else:
        print("loosen -----------------------------")
        #input("countinue game Y , N")
        if input("countinue game Y , N  :") == "Y":
            i = randint(1, 40)
            game(i)


# print(data[i][people])
i = randint(1, 40)
game(i)
