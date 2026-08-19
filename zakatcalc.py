#Zakat Calculator

print("Welcome to the Zakat Calculator")
sum = 0

#Notes
#Later ... will add the option to do different currencies
#Get API - MetalPriceAPI and link it to program
#If someone does not own any assets except from Gold, then the nisab value of gold must be used

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
def crops():
    global sum
    harvest = int(input("Please enter total amount of harvest yielded in kg: "))
    while True:
        if (harvest >= 612):
            agric_zakat(harvest)
            break
        elif (harvest < 612):
           print("Your crops are not Zakat eligible")
           break
        else:
            break
        
# Money u owe
def owing():
    global sum
    owing = int(input("How much money are you owing: "))
    sum -= owing
        
#Updated Gold function
def gold_to_cash():
    global sum
    gold = float(input("Please enter total pure gold weight you own in grams: "))
    nisab_gold = 87.48
    
    while True:
        if (gold < nisab_gold and sum == 0):
            print("Your gold is not zakat taxable!")
            break
        
        elif (gold >= nisab_gold and sum == 0):
            cashvalue_gold = gold * 105.27
            loneasset_gold(cashvalue_gold)
            break
        
        else:
            break
            
    cashvalue_gold = gold * 105.27 #Later adapt value e.g (104.28) based on carat value of gold
    sum += cashvalue_gold
    

#If gold is the only asset
def loneasset_gold(cashvalue_gold):
    while True:
        if (cashvalue_gold >= 9209.26):
            zakat_payable(cashvalue_gold)
            break


#Hanafi madhab - nisab market value of silver
def surplus_wealth():
    global sum
    nisab_silver = 942.58 #nisab_silver changes
    if (sum >= nisab_silver):
       zakat_payable(sum)
    else:
        print("The total amount of wealth you have is NOT Zakat payable")

#Calculate zakat amount eg 2.5%
def zakat_payable(sum):
    zakat_pay = sum * 0.025 
    print("The amount of Zakat due for you to pay is ", round(zakat_pay))
    pass

#Calculate zakat on agricultural products    
def agric_zakat(harvest):
   irrigation = input("Please enter method of irrigation used to harvest")
   while True: 
       if irrigation.casefold() == "natural":
           zakat_agric = harvest * 0.10
           print("Zakat due on argicultural produce is ", zakat_agric)
           break

       elif irrigation.casefold() == "artificial":
           zakat_agric = harvest * 0.05
           print("Zakat due on argicultural produce is ", zakat_agric)
           break

       elif irrigation.casefold() == "mixed":
           zakat_agric = harvest * 0.075
           print("Zakat due on argicultural produce is ", zakat_agric)
           break
        


#Run
cash_savings()
##gold()
#silver()
investments()
assets()
iou()
#crops()
owing()
gold_to_cash()
crops()

#Program handling
print("Total amount you have is: ", round(sum, 2))

surplus_wealth()
