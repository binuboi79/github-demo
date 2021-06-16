#Add addition implementation
def add(x,y):
    return x+y
#Add subtraction implementation
def subtract(x,y):
    return x-y
#Add multiplication implementation
def multiply(x,y):
    return x*y
#Add division implementation
def divide(x,y):
    if x<0:
	return NEGATIVE_ANS
    if y==0:
	return DIVIDE_BY_0_ERROR
    else:
	return x/y

