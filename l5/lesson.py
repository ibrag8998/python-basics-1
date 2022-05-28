# age = int(input())
# print(age)

###

# try:
#     a = int(input())
# except ValueError:
#     print("?")

# print(a)

###

# try:
#     a = int(input())
# except ValueError:
#     print("?")
# else:
#     print(a)

###

# try:
#     a = int(input())
# except ValueError:
#     print("?")
# else:
#     print(a)
# finally:
#     print("spasibo dosvidaniya")

###

# try:
#     a = int(input())
# except ValueError as e:
#     print(e)

###

# def f(raw):
#     try:
#         a = int(raw)
#     except (ValueError, TypeError) as e:
#         print(e)
#     # except (ValueError, TypeError) as e:
#     #     print(e)
   
# f("asd")
# f(None)

###

# class MyException(Exception):
#     ...
    
# def send_request():
#     ...
    
# def parse_response():
#     ...
    
# def get_data_from_internet():
#     response = send_request()
#     if response.status_code != 200:
#         raise MyException("status code:", response.status_code)
#     data = parse_response(response)
#     return data
    
# try:
#     data = get_data_from_internet()
# except MyException:
#     print("cannot get data from internet")

###

# try:
#     int(None)
# except ValueError:
#     print("!@#!@#")
# except TypeError:
#     print("type error")

###

# def do_math(a, b):
#     return a / b

# try:
#     print(do_math(1, 0))
# except ZeroDivisionError:
#     print("на 0?..")
# except ArithmeticError as e:
#     print("arithmetic error", e)

###

# Конец #


# Модули, import

# alias

# import another_module as abc

# abc.f()
# print(abc.MyClass)

###

# from another_module import MyClass as MySuperClass
# from another_module import f

# f()
# print(MySuperClass())

###

# from another_module import f

# f()

###

# Структура python-проектов

# import package.package_module

# package.package_module.g()
# package.package_module.call_h()


# $PYTHONPATH = "/home/ibrahim/project/python-basics-1/l5/"
# $PYTHONPATH = "/home/ibrahim/project/python-basics-1/l5/package/"

###

# from package import call_h, g

# call_h()
