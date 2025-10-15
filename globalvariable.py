#global variable
#global keyword

rno=101 #global variable
def show():
    #global rno
    #print("roll no in the function:",rno)
    #local variable
    #rno=123
    rno=123
    print("Roll no inside the function after changes:",rno)
#call the function
show()
print("roll no outside the function:",rno)
