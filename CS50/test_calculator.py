from calculator import square

# def test_square():
#     try:
#         x = int(input('\nCheck square\n\nNumber: '))
#         squared = int(input('Square: '))
#         assert square(abs(x)) == squared
#     except AssertionError:
#         print('{} squared was not {}'.format(x, squared))
#     return x, squared
                
# test_square()

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
    
    
    
    