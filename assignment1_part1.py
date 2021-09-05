def listDivide(numbers, divide=2):
    """The function returns the number of elements in the numbers list that are divisible
    by divide.
    """
    divisible = []
    for x in numbers:
        if x % divide == 0:
            divisible.append(x)
    return(len(divisible))


class ListDivideException(Exception):
    pass


def testListDivide():
    """This function tests some parameters in the listDivide function to make sure it is working
    """
    try:
        if listDivide([1,2,3,4,5]) != 2:
            raise ListDivideException
        if listDivide([2,4,6,8,10]) != 5:
            raise ListDivideException
        if listDivide([30,54,63,98,100],10) != 2:
            raise ListDivideException
        if listDivide([]) != 0:
            raise ListDivideException
        if listDivide([1,2,3,4,5],1) != 5:
            raise ListDivideException
    except ListDivideException:
        print("Something in your math is wrong")

testListDivide()