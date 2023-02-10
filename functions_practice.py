def hello():
    print("Hi!")

def pack(item, item_2, item_3):
    return [item, item_2, item_3]

def eat_lunch(a_list):
    if a_list == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(a_list)):
            if i == 0:
                print(f"First I eat {a_list[0]}")
            else: 
                print(f"Next I eat {a_list[i]}")


hello()
eat_lunch(pack("chips", "apple", "sandwhich"))


