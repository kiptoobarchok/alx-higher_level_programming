# 0x0A. Python - Inheritance


# Resources
*Read or watch*:

[Inheritance](https://intranet.alxswe.com/rltoken/ct-bhZHBxfE-aHYQoAcscQ)

[Multiple inheritance](https://intranet.alxswe.com/rltoken/qq52YyYhDIbKBneA-u0PKw)

[Inheritance in Python](https://intranet.alxswe.com/rltoken/RJVbH9PvRlwDkBxcTloVOQ)

[Learn to Program 10 : Inheritance Magic Methods](https://intranet.alxswe.com/rltoken/CFBGj9h1gP3eNLnEm2Ehhg)


# Task : 0. Lookup

Write a function that returns the list of available attributes and methods of an object:

    Prototype: def lookup(obj):
    Returns a list object
    You are not allowed to import any module


# Advanced Tasks
   # 12. My integer

Write a class MyInt that inherits from int:

    MyInt is a rebel. MyInt has == and != operators inverted
    You are not allowed to import any module:
     
        guillaume@ubuntu:~/0x0A$ cat 100-main.py
        #!/usr/bin/python3
        MyInt = __import__('100-my_int').MyInt

        my_i = MyInt(3)
        print(my_i)
        print(my_i == 3)
        print(my_i != 3)

        guillaume@ubuntu:~/0x0A$ ./100-main.py
        3
        False
        True
        guillaume@ubuntu:~/0x0A$ 
