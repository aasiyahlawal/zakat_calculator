#Zakat Calculator

print("Welcome to the Zakat Calculator")
sum = 0

#Notes
#Later ... will add the option to do different currencies
#Get API - MetalPriceAPI and link it to program
#If someone does not own any assets except from Gold, then the nisab value of gold must be used

#Pseudocode
# zakatable_items = [cash, gold, silver, etc]
#for items in zakatable_items:
#   input("Please enter total amount of ", item "you have")
#       blah blah blah, do stuff
#   if zakatable_items[items] == gold || silver
#       create a loop to check if it meets nisab value


#Cash & Savings
def cash_savings():
    global sum
    cashsav = int(input("Please enter total amount of cash and savings you have: "))    
    sum += cashsav
        

#Silver
def silver():
    global sum
    silver = int(input("Please enter total grams of silver weight you own: "))
    while True:
        if (silver < 612.36):
            print("Your silver is not zakat taxable")
            break
        else:
            sum += silver
            break

#Investments and stocks
def investments():
    global sum
    invest = int(input("Please enter total cash value of investment and stocks held by you: "))
    sum += invest

#Business Assets
def assets():
    global sum
    assets = int(input("Please enter business assets owned by you: "))
    sum += assets

#IOU (Money owed to u)
def iou():
    global sum
    iou = int(input("Please enter total amount owed to you: "))
    sum += iou

# Agric produce & livestock
def agric():
    #write
    pass

# Money u owe
def owing():
    global sum
    owing = int(input("How much money are you owing: "))
    sum -= owing

#Gold and silver
def gold():
    global sum
    gold = int(input("Please enter total pure gold weight you own: "))
    nisab_gold = 87.48 #possible just use the nisab gold value, to reduce number of variables
    while True:
        if (gold < nisab_gold):
            print("Your gold is not zakat taxable!")
            break
        else:
            sum += gold
            break
        
#Updated Gold function
def gold_to_cash():
    global sum
    gold = input("Please enter total pure gold weight you own in grams: ")
    nisab_gold = 87.48 
    while True:
        if (gold < nisab_gold and sum == 0):
            print("Your gold is not zakat taxable!")
            break
        elif (gold < nisab_gold and sum == 0):
            #call function nisab_gold()
    cashvalue_gold = gold * 104.28 #Later adapt value e.g (104.28) based on carat value of gold

#If gold is the only asset
def nisab_gold():
    break


#Hanafi madhab - nisab market value of silver
def surplus_wealth():
    global sum
    nisab_silver = 941.29 #nisab_silver changes
    if (sum >= nisab_silver):
       zakat_payable(sum)
    else:
        print("The total amount of wealth you have is NOT Zakat payable")

#Calculate zakat amount eg 2.5%
def zakat_payable(sum):
    #zakat_pay = 2.5% * sum
    zakat_pay = sum * 0.025 
    print("The amount of Zakat due for you to pay ", zakat_pay)
    pass


#Run
cash_savings()
gold()
silver()
investments()
assets()
iou()
agric()
owing()

#Program handling
print("Total amount you have is: ", sum)

surplus_wealth()
