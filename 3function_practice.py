def name_args(**kwargs):
  for k in kwargs.keys():
    print(f"{k}:{kwargs[k]}")

name_args(name="Randon", weather="sunny",location="park",time=3)

def all_true(iter):
  return all(iter)

print(all_true((True, False)))

def one_true(iter):
  return any(iter)

print(one_true((True, False)))

def recursive_factorial(n):
  if n <= 1:
    return 1
  else:
    return n * recursive_factorial(n-1)

print(recursive_factorial(6))

def recursive_deduplicate(my_str,i=0):
  if len(my_str) <= 1 or i == len(my_str)-1:
    return my_str
  else:
    if my_str[i] == my_str[i+1]:
      return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
    else:
      return recursive_deduplicate(my_str,i+1)
      
print(recursive_deduplicate("Guayaba"))

def recursive_reverse(str, i=0):
  if len(str)==0:
    return ""
  elif i == len(str)-1:
    return str[0]
  else:
    return str[-1-i] + recursive_reverse(str, i+1)

print(recursive_reverse("Mamoncillo"))
  