print("Hello World")

###

int  # целое число (1)
float  # вещественное число (1.2)
str  # строка ("ASD")

a = 1  # int
b = 123.32
s = "asd"

print(type(b))

print(a + b)
# Выводит ошибку:
# print(a + s)

###

b = True  # bool (boolean)
True | False
n = None  # null, nil

l = ["asd", 1.23, 23, [123, "123"], True, None]
# user
d = {
    "username": "ibragdzh",
    "age": 20,
}
l2 = [
    ["username", "ibragdzh"],
    ["age", 20],
]

print(l)
print(d)

###

s = "string"  # str
caps_s = s.upper()
print("s = ", s)
print(caps_s)
lower_s = caps_s.lower()
print(lower_s)

###

# 0, 1, 2
l = []
l.append(1)
print(l)
l.append(None)
print(l)

# Сейчас l = [1, None]

l.insert(1, True)
print(l)

another_l = [1, 2, 3]

l.extend([3, 5])
print(l)

print(l[2])

###

user = {
    "username": "ibragdzh",
    "age": 20,
    # дальше бессмысленные поля, просто так
    True: None,
    None: False,
    2: 2.3,
    "list": [1, 3],
    "nested_dict": {
        "list": [
            {},
        ]
    },
}

age = user["age"]
print(age)
print(user[2])

###

a = input()
print(type(a))

###

# if, for, while

gender = input("Введите ваш пол: ")

if gender == "M":  # male
    print("male")
elif gender == "F":  # female
    print("female")
else:
    print("unknown")

###

list | dict  # collections
l = [1, 2, 3, 4, 5]

for i in l:
    print(i * i)

i = 0
while i < 5:
    print(i)
    i = i + 1

###

# continue, break

# Спрашивать инпут до тех пор, пока он не равен "0"

while True:
    a = input("Введите что-нибудь: ")
    if a == "0":
        break

# Спрашивать инпут и выводить его до тех пор, пока он не равен "0",
# а когда равен, не выводить ничего

while True:
    a = input("Введите что-нибудь: ")
    if a == "0":
        continue
    print(a)

###
