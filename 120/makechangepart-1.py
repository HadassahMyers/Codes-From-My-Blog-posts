amntForWhichChangeIsToBeFound = 11
coinsWeHaveUsingwhichChangeHastoBeFound = [1,2,5]
LastcoinUsedToGetChangeArray = [0]*(amntForWhichChangeIsToBeFound+1)  
numberOfCoinsUsedForChange = [0]*(amntForWhichChangeIsToBeFound+1)
coinCount = 11
LastCoinUsedforChange = 1
numberOfCoinsUsedForChange[9] = 3 
numberOfCoinsUsedForChange[10] = 2
numberOfCoinsUsedForChange[6] = 2 

for j in [c for c in coinsWeHaveUsingwhichChangeHastoBeFound if c<=amntForWhichChangeIsToBeFound]:
    if numberOfCoinsUsedForChange[amntForWhichChangeIsToBeFound - j] + 1 < coinCount:
	    coinCount = numberOfCoinsUsedForChange[amntForWhichChangeIsToBeFound - j] + 1
	    LastCoinUsedforChange = j 
numberOfCoinsUsedForChange[amntForWhichChangeIsToBeFound] = coinCount 
LastcoinUsedToGetChangeArray[amntForWhichChangeIsToBeFound] = LastCoinUsedforChange 
print (numberOfCoinsUsedForChange)
print (LastcoinUsedToGetChangeArray)