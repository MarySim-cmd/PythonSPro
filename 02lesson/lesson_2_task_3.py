import math
def square(side):
    area = side ** 2
    return area if isinstance(side, int) else math.ceil(area)
if __name__ == "__main__":
    print(square(5))     
    print(square(5.0)) 
    print(square(5.1))
    print(square(5.5))
    print(square(3)) 
    print(square(3.7))