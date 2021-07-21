# Display a 3X3 Grid 

for row in range(7):
    for col in range(10):
        if (row==0 or row==2 or row==4 or row==6) and (col==0 or col==3 or col==6 or col==9):
            print("+", end="")
        elif (row==1 or row==3 or row==5) and (col==0 or col==3 or col==6 or col==9):
            print("|",end="")
        elif (row==1 or row==3 or row==5) and (col==1 or col==2 or col==4 or col==5 or col==7 or col==8):
            print(" ",end="")
        else:
            print("-", end="")
    print("")
    
