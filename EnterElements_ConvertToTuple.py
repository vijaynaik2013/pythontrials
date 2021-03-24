if __name__ == '__main__':
    N = int(input("please enter the number of digits"))
    integer_list = map(int, input("please enter the elements in list").split())
    b = (tuple(integer_list))
    print(hash(b))



