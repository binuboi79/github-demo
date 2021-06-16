#Add addition implementation
#new head
def add(x,y):
    return x+y
#Add subtraction implementation
#new head
def subtract(x,y):
    return x-y
#Add multiplication implementation
#new head
def multiply(x,y):
    return x*y
#Add division implementation
#new head
def divide(x,y):
    if x<0:
	return NEGATIVE_ANS
    if y==0:
	return DIVIDE_BY_0_ERROR
    else:
	return x/y

