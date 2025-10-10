#case sensitive variable names
'''

a=7
A='sandy'
print(a,A)

'''
#unpacking
'''

games=['cricket','football','kabaddi']
a,b,c=games
print(a,b,c)
print(a + b + c)
print(a)
print(b)
print(c)

'''
#note:look at the space between single quote for the word'he'
'''

x='he '
y='is'
z='okey'
print(x+y+z)

'''
#create a variable inside a function,with the same name as the global variable
'''

x="wow"
def myfunc():
    x='super'
    print(x)
myfunc()
print(x)

'''
