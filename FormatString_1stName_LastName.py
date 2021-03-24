def print_full_name(a,b):
  #  fullname = f"{first_name} {last_name}"
    fullname = f"Hello {a} {b}! you just delved into python."
    print (fullname)

if __name__ == '__main__':
    first_name = str(input("please enter first name:"))
    last_name = str(input("please enter second name:"))
    print_full_name(first_name, last_name)



