#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("James", "Maddison")
say_my_name("Martin")
say_my_name("Diogo", "Jota")
try:
    say_my_name("Richard",10)
except Exception as e:
    print(e)
