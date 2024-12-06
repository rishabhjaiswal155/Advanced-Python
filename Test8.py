#deleting static variables

class Test8:
    c=30
    a=10
    b=20
    def __init__(self):
        del Test8.a
    @classmethod
    def m2(cls):
        del cls.b
        del Test8.c
t=Test8()
t.m2()
