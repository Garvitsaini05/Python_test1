print("Enter Month")
month=int(input(":- "))
print("Enter Day")
day=int(input(":- "))
print("Enter Year")
year=int(input(":- "))

if day>31:
    print("ERROR: Invalid Day Input")
if month>12:
    print("ERROR: Invalid Month Input")
if year>99:
    print("ERROR: Invalid Year Input")

if month==2:
    if year%4 == 0:
        if day>29:
            print("ERROR: Invalid Day Input")
        else:
            print("SUCCESS: Congratulations! You entered a correct date.")
            print("The Entered Date is :- ", month ,"/", day ,"/", year)
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    if day>31:
        print("ERROR: Invalid Day Input")
    else:
        print("SUCCESS: Congratulations! You entered a correct date.")
        print("The Entered Date is :- ", month ,"/", day ,"/", year)
if month==4 or month==6 or month==9 or month==11:
    if day>30:
        print("ERROR: Invalid Day Input")
    else:
        print("SUCCESS: Congratulations! You entered a correct date.")
        print("The Entered Date is :- ", month ,"/", day ,"/", year)