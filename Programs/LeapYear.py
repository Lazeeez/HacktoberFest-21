# Checkes if a given year is leap year or not

# To determine whether a year is a leap year, follow these steps:
    # Step 1: If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5
    # Step 2: If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4
    # Step 3: If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5
    # Step 4: The year is a leap year (it has 366 days)
    # Step 5: The year is not a leap year (it has 365 days)

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