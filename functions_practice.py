def hello():
    print("Hello User")


def pack(a,b,c):
    set1 = {a,b,c}
    listed = list(set1)
    print(listed)


def eat_lunch(list):
    if len(list) == 0:
        print('My lunch box is empty')
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First i eat {list[0]}")
            else:
                print(f"Next i eat {list[i]}")


hello()

pack('leonel', 'lamelas', '23')

eat_lunch(["Guaba"])
eat_lunch(["tamarindo","Salmon","Bistec","Higado"])