# p 1008
# contorl the float decimal point 
# in case of C or C++ -> consider the data type. ex) float(4)/ float(5)
# in case of python -> you don't need to consider the data type

def print_divide(dividend,divisor):
    print("%0.9f" % (dividend/divisor))


dividend, divisor = map(int, input().split())
print_divide(dividend, divisor)

