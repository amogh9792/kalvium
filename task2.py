# The minimum_coins function takes in 3 parameters:
# change: the amount of change to return
# denominations: a list of coin denominations to use for the change
# available_coins: a dictionary that maps each denomination to the number of coins available for that denomination
# The function first sorts the denominations in descending order, and then iteratively subtracts the largest denomination
# possible from the change until it becomes 0. The coins used for the change are stored in the coins list.
# If the change cannot be given with the available coins, the function returns None.

def minimum_coins(change, denominations, available_coins):
    coins = []
    for denomination in sorted(denominations, reverse=True):
        while change >= denomination and available_coins[denomination] > 0:
            change -= denomination
            coins.append(denomination)
            available_coins[denomination] -= 1
    if change != 0:
        return None # Change cannot be given
    return coins

# Example usage with British Pound denominations
print("Enter the amount")   #Taking input of the amount
amount=int(input())
print("Enter the currency") #Taking input of the currency
currency=input()
currency=currency.lower()
if(currency=="british pound"):  #condition for currency

    denominations = [1, 2, 5, 10, 20, 50]
    available_coins = {1: 10, 2: 10, 5: 10, 10: 10, 20: 10, 50: 10}
    result = minimum_coins(amount, denominations, available_coins) #calling minimum coin function
elif (currency == "us dollar"):
    denominations = [1, 5, 10, 25]
    available_coins = {1: 10, 2: 10, 5: 10, 10: 10, 20: 10, 50: 10}
    result = minimum_coins(amount, denominations, available_coins)
elif (currency == "norwegian krone"):
    denominations = [1, 5, 10, 20]
    available_coins = {1: 10, 2: 10, 5: 10, 10: 10, 20: 10, 50: 10}
    result = minimum_coins(amount, denominations, available_coins)
else:
    print("Invalid currency")



if result is None:
    print("Change cannot be given.")
else:
    print("Coins:", result)


