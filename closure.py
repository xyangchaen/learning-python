def f1(x):
    def f2(y):
        return x+y
    return f2
x=print(f1(1)(2))
