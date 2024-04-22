#conver decimal to binary
#example 10 ->

def decimalToBinary(num):

    binaryString = ""

    def binaryDivisionHelper(num):
        nonlocal binaryString
        if num < 2:
            binaryString += str(num)
        else:
            binaryDivisionHelper(num//2)
            binaryDivisionHelper(num % 2)
    binaryDivisionHelper(num)
    return binaryString

print(decimalToBinary(2))
