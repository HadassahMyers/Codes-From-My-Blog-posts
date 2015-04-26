def printCoins(amntForWhichChangeIsToBeFound,LastcoinUsedToGetChangeArray):
    coin = amntForWhichChangeIsToBeFound
    while coin > 0:
        LastCoinForCoinCent = LastcoinUsedToGetChangeArray[coin]
        print(LastCoinForCoinCent)
        coin = coin - LastCoinForCoinCent

def main():
    amntForWhichChangeIsToBeFound = 68
    #edit it for the value you want it for 
    coinsWeHaveUsingwhichChangeHastoBeFound = [1,5,10,21,25]
    LastcoinUsedToGetChangeArray = [0]*(amntForWhichChangeIsToBeFound+1)  
    numberOfCoinsUsedForChange = [0]*(amntForWhichChangeIsToBeFound+1)
    for cents in range(amntForWhichChangeIsToBeFound+1):
    	#This loop starts finding change from 1 cent, then 2,3,4..amntForWhichChangeIsToBeFound
        coinCount = cents
        LastCoinUsedforChange = 1
        for j in [c for c in coinsWeHaveUsingwhichChangeHastoBeFound if c <= cents]:
            if numberOfCoinsUsedForChange[cents - j] + 1 < coinCount:
    	        coinCount = numberOfCoinsUsedForChange[cents - j] + 1
    	        LastCoinUsedforChange = j 
        numberOfCoinsUsedForChange[cents] = coinCount 
        LastcoinUsedToGetChangeArray[cents] = LastCoinUsedforChange 
    #print (numberOfCoinsUsedForChange)
    #print (LastcoinUsedToGetChangeArray)	
    print("Number of coins used: "+ str(numberOfCoinsUsedForChange[amntForWhichChangeIsToBeFound]))
    print("Here are the coins used ")
    printCoins(amntForWhichChangeIsToBeFound, LastcoinUsedToGetChangeArray)

main()