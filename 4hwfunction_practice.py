def max_num(a,b,c):
    list1 = [a,b,c]
    print('max numer', max(list1))

max_num(120,520, 50)

def mult_list(lst):
 
  if len(lst) == 0:
    return 0

  prod = lst[0]

  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod
    
print(mult_list([1,2,3]))


def reverse_string(txt):
  txt = txt[::-1]
  print(txt)

reverse_string("Hello")

def num_within(x,a,b):
  return x in range(a,b+1)

print(num_within(3,1,3))

def pascals(n):
  for i in range(n+1):
    for j in range(n-i):
      print('', end='')

    c = 1
    for j in range(1, i+1):
        print(c, '', end='')
        c = c * (i - j) // j
    print()

pascals(10)