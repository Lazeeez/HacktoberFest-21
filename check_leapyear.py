# Python program to check if year is a leap year or not

year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

 year = int(input())
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(str(year) +" is a leap year")
        else:
           print(str(year) +" is not a leap year")
           
    else:
        print(str(year) +" is a leap year")
else:
     print(str(year) +" is not a leap
