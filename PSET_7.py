import math
import sys
sys.setrecursionlimit(10000)

def trade_turkey(prices, k):
    """"Find the optimal way to buy and sell turkeys to maximize 
    the total profit.

    Args:
        prices: a list of turkey prices, where prices[i] is the price
        of a turkey on day i.
        k: the maximum number of turkeys you can buy

    Returns:
        a list of up to k non-overlapping trades that gives you the
        max total profit, where each trade is of format (buy_index, sell_index)
    """
    #bottom up
    maps = {}
    for m in range(k+1): #set up map
        maps[(len(prices),-1,m)] = (0,[])
        maps[(len(prices),1,m)] = (0,[])
    for i in range(len(prices)-1,-1,-1): #now bottom up make the X values
        #b=1, for having a turkey here, want to sell
        for m in range(k+1): #for now, can do anything
            if maps[(i+1,1,m)][0] > prices[i]+maps[(i+1,-1,m)][0]:
                maps[(i,1,m)] = maps[(i+1,1,m)]
            else: #sell
                maps[(i,1,m)] = (maps[(i+1,-1,m)][0]+prices[i],[i]+maps[(i+1,-1,m)][1]) 
        #b=-1, for not having a turkey here, want to buy
        for m in range(k): #for now, can do anything
            if maps[(i+1,-1,m)][0] > maps[(i+1,1,m+1)][0]-prices[i]:
                maps[(i,-1,m)] = maps[(i+1,-1,m)]
            else: #buy
                maps[(i,-1,m)] = (maps[(i+1,1,m+1)][0]-prices[i],[i]+maps[(i+1,1,m+1)][1])
        #now do k, which cannot buy a turkey, so only skip
        maps[(i,-1,k)] = maps[(i+1,-1,k)]
    output = []
    for i in range(0,len(maps[(0,-1,0)][1]),2):
        output.append((maps[(0,-1,0)][1][i],maps[(0,-1,0)][1][i+1]))
    return output
