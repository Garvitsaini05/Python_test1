print("PRIMARY COLOURS :- red , yellow , blue")
print("")
print("Enter First primary Color (IN LOWER_CASE LETTERS ONLY)")
color_1=input(":- ").lower()
print("Enter Second primary Color (IN LOWER_CASE LETTERS ONLY)")
color_2=input(":- ").lower()

if color_1=="red" or color_1=="blue" or color_1=="yellow":
    print("")
else:
    print("Error: Invalid Colour.1")
if color_2=="red" or color_2=="blue" or color_2=="yellow":
    print("")
else:
    print("Error: Invalid Colour2.")

if color_1=="red":
    if color_2=="blue":
        print( "red" ,"+", "blue" ,"=", "PURPLE")
if color_1=="red":
    if color_2=="yellow":
        print("red" ,"+", "yellow" ,"=", "ORANGE")
if color_1=="blue":
    if color_2=="yellow":
        print("blue" ,"+", "yellow" ,"=", "GREEN")
if color_1=="yellow":
    if color_2=="blue":
        print("yellow" ,"+", "blue" ,"=", "GREEN")
if color_1=="yellow":
    if color_2=="red":
        print("blue" ,"+", "yellow" ,"=", "ORANGE")
if color_1=="blue":
    if color_2=="red":
        print("blue" ,"+", "red" ,"=", "PURPLE")
