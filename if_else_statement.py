if 10>5:
    print("Hell");print("O")
    print("1")
    print('2')
    
    print('3')
    
 #3   
num = 7
if num > 3:     #TRUE
    print("3")  
    if num > 5: #FALSE
        print("5")
        if num == 7:  #IGNORE
            print("7")
            
 
num = 7
if num > 3: #TRUE
    print("3")
    if num <5 :    #TRUE
        print("5")
        if num == 7:  #TRUE
            print("7")     
            

#Else statement
if num >7:
    print(">7") 
else:
    print("<7") 
        
#every if condition block can have only one else statement.or you can make a chain
num = 3
if num == 1 :
    print("one")
else:        
    if num == 2:
        print("Two")
    else:
        if num == 3:
            print("Three")
        else:
            print("others")
        
#else if = elif，shortcut to use 
num = 3
if num == 1 :
    print("one")
elif num == 2:
    print("TwO")
elif num == 3:
    print("Three")
else:
    print("others")
            
            