#a script to determine the weight of any dollar amount in any form

def dollarCheck():
    global startval
    startval = input("amount of money (in dollars): ")
    try:
        startval = int(startval)
    except:
        print("\ninvalid input.\n")
        dollarCheck()
        

def recurCheck():
    global convtype
    inp = input("currency to change it to: ").lower().strip()
    if inp == "pennies" or inp == "nickels" or inp == "dimes" or inp == "quarters" or inp == "50_cent_pieces" or inp == "golden_dollars" or inp == "dollar_bills" or inp == "2_dollar_bills" or inp == "5_dollar_bills" or inp == "10_dollar_bills" or inp == "20_dollar_bills" or inp == "50_dollar_bills" or inp == "100_dollar_bills":
        convtype = inp
    elif inp == "help":
        print("\ninput keywords:\npennies\nnickels\ndimes\nquarters\n50_cent_pieces\ndollar_coins\ndollar_bills\n2_dollar_bills\n5_dollar_bills\n10_dollar_bills\n20_dollar_bills\n50_dollar_bills\n100_dollar_bills\n")
        recurCheck()
    else:
        print("invalid input. (type help for supported keywords)")
        recurCheck()

#weight is measured in pounds because i'm a rube, it will be additionally converted to kilograms at the end        
def calc():
    if convtype == "pennies":
        multiplier = 100
        weight = 0.00551156
    elif convtype == "nickels":
        multiplier = 20
        weight = 0.0110231
    elif convtype == "dimes":
        multiplier = 10
        weight = 0.0050000841
    elif convtype == "quarters":
        multiplier = 4
        weight = 0.01250021
    elif convtype == "50_cent_pieces":
        multiplier = 2
        weight = 0.0171961
    elif convtype == "golden_dollars":
        multiplier = 1
        weight = 0.0178574
    elif convtype == "dollar_bills":
        multiplier = 1
        weight = 0.00220462
    elif convtype == "2_dollar_bills":
        multiplier = .5
        weight = 0.00220462
    elif convtype == "5_dollar_bills":
        multiplier = .2
        weight = 0.00220462
    elif convtype == "10_dollar_bills":
        multiplier = .1
        weight = 0.00220462
    elif convtype == "20_dollar_bills":
        multiplier = .05
        weight = 0.00220462
    elif convtype == "50_dollar_bills":
        multiplier = .02
        weight = 0.00220462
    elif convtype == "100_dollar_bills":
        multiplier = .01
        weight = 0.00220462

    lbsAns = startval * multiplier * weight
    kilosAns = lbsAns / 2.205

    print(f"{startval} dollars in {convtype} would weigh {lbsAns} pounds, or {kilosAns} kilograms.")
        
        

    
dollarCheck()
recurCheck()
calc()
