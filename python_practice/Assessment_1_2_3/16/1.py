def swapList(num):
    #size = len(num)

    num[0], num[-1] = num[-1], num[0]

    return num

num = [12, 35, 9, 56, 24]
print(swapList(num))