
#def add(a,b):
 #   return a+b
#def sub(a,b):
 #   return a-b

#if __name__ == "__main__":
 #   print(add(1, 4))
 #   print(sub(4, 2))

class FourCal:

    def __init__(a, b, c):
        a.b = b
        a.c = c
        
    def add(a):
        return a.b+a.c
    def sub(a):
        return a.b-a.c
    def mul(a):
        return a.b*a.c
    def div(a):
        return a.b/a.c
