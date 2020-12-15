def get_square(x):
    """Return: square only for int, float, complex.
       Errors: raise ValueError if int=0
               raise TypeError in other type.
    """
    if type(x) in (int, float, complex):
        if type(x) == complex and x.imag == 0 or x.real == 0:
            raise ValueError("Complex = o!")
        if type(x) == int and x == 0:
            raise ValueError("Int = o!")
        return pow(x, 2)
    else:
        raise TypeError("Type only int, float, complex!")
