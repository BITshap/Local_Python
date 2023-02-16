def arguements(*args):
    for i in args:
        print(i)

def inner_func(a, b):
    def inner_1():
        return a+b
    def inner_2():
        return a-b
    print(inner_1()+inner_2())

def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)

def sum_n_product(a, b):
    print(a+b, a*b)

alias_arb_args = arguements

def arb_mean(*args):
  total = 0
  for a in args:
    total += a
  print(a/len(args))

def arb_longest_string(*args):
  long = 0
  longest = ""
  for a in args:
    if len(a) > long:
      long = len(a)
      longest = a
  print(longest)

arguements(1,2)
lunch_lady("Nick")
inner_func(5,6)
arb_mean(1,4,5)
arb_longest_string("Nick", "Cameron", "Corey")


        

