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


    # 13. Can I?
Write a function that adds a new attribute to an object if it’s possible:

    Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
    You are not allowed to use try/except
    You are not allowed to import any module
        guillaume@ubuntu:~/0x0A$ cat 101-main.py
        #!/usr/bin/python3
        add_attribute = __import__('101-add_attribute').add_attribute

        class MyClass():
            pass

        mc = MyClass()
        add_attribute(mc, "name", "John")
        print(mc.name)

        try:
            a = "My String"
            add_attribute(a, "name", "Bob")
            print(a.name)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

        guillaume@ubuntu:~/0x0A$ ./101-main.py
        John
        [TypeError] can't add new attribute
        guillaume@ubuntu:~/0x0A$ 