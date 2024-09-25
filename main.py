# gets number inputs
num1 = input("Enter number here: ")  
num2 = input("Enter number here: ") 
num3 = input("Enter number here: ") 

#checks number input
if num1 > num2:
    if num1 > num3:
        gnum = num1
        if num2 > num3:
            mnum = num2
            snum = num3
            print (gnum, " is the largest number.", mnum, " is the second largest", snum, " is the smallest number")
        else:
            mnum = num3
            snum = num2
            print (gnum, " is the largest number.", mnum, " is the second largest", snum, " is the smallest number") 
    else:
        gnum = num3, mnum = num1, snum = num2
        print (gnum, " is the largest number.", mnum, " is the second largest", snum, " is the smallest number") 
else:
    if num2 > num3:
        gnum = num2
        if num1 > num3:
            mnum = num1
            snum = num3
            print (gnum, " is the largest number.", mnum, " is the second largest", snum, " is the smallest number") 
        else:
            mnum = num3
            snum = num1
            print (gnum, " is the largest number.", mnum, " is the second largest", snum, " is the smallest number") 
    else:
        gnum = num3, mnum = num2, snum = num1
        print (gnum, " is the largest number.", mnum, " is the second largest", snum, " is the smallest number") 