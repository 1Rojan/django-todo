# def inc(num):
#     return num+1
#
# def dec(num):
#     return num-1
#
# def higher_order(func, x):
#     return func(x)
#
#
# print(higher_order(inc, 22))


# --Decorator--

# def ordinary():
#     print("I am ordinary")
#
# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
# ordinary()
# a = make_pretty(ordinary)
# print(a())
# def another_function():
#     print("another function")
#
# def turn_into_another_function(fnc):
#
#      return another_function
#
# @turn_into_another_function
# def a_function():
#     print("a_function")
#
# # a_function = turn_into_another_function(a_function)
# a_function()
#
#
#
# def camel_case(*s):
#     print(s)
#     camel = ''.join([word.capitalize() for word in s.split('_')])
#     print(camel)
#
# names = [
#     "rojan_sunar",
#     "sunar_rojan"
# ]
#
# camel_case(names)
#
# # camel_case("Snake_case")



class Person:
    TITLES = ('Dr', 'Mr', 'Mrs')
    deceased = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def mark_as_deceased(self):
        self.deceased = True

person_obj = Person("Rojan", 27)
print(person_obj.TITLES)
print(person_obj.mark_as_deceased())
print(person_obj.deceased)

person2 = Person("Sunar", 22)
print(person_obj.deceased)
