
def arb_args(*args):
  for a in args:
    print(a)

def inner_func(x,y):
  def inner_1():
    return x+y
  def inner_2():
    return x-y
  print(inner_1()+inner_2())


def lunch_lady(name, lunch="Mystery Meat"):
  print(name, lunch)

def sum_n_product(x,y):
  return x+y,x*y

alias_arb_args = arb_args

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
  return longest

