print(1 + 2)
print(7 / 3)
print(7 // 3)
print(3**2)
print(type(10), type("hello"), type(3.14))

a = [1, 2, 3, 4, 5]
print(a, len(a), a[0])
a[4] = 100
print(a)

# スライシング
print(a[2:])  # 3, 4, 100
print(a[1:-1])  # 2, 3, 4
print(a[3:4])  # 4
print(a[-3])

# ディクショナリ
me = {"height": 180, "weight": 55}
print(me)
me["hoge"] = "piyo"
print(me)

# boolean
isTrue = False
print(type(isTrue))
print(not isTrue)
if True and True or False and not False:
    print("こんにちは")

# for
for i in range(1, 101):
    print(f"{i}, ", end="")
print()


# function
def hello(string: str):
    print("こんにちは,", string)


hello("suzuki")


# class
class Car:
    def __init__(self, number):
        self.number = number

    def hello(self):
        print("hello, world")


c = Car(333)
print(c.number)
c.hello()
