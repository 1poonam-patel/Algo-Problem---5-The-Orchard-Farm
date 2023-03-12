f = open("TOF_large.txt",'r')
t = int(f.readline())

f2 = open("problem-5_output_small.txt",'w')

for i in range(t) :
    line = f.readline()
    if line[-1] == '\n' :
        line = line[:-1:].split("\t")
    else :
        line = line.split("\t")
    n = int(line[0])
    d = int(line[1])
    useDays = n

    l = {'apple':12000, 'orange':10000, 'mango':27500, 'lemon':7500, 'coconut':8000}
    days = {'apple':10, 'orange':6, 'mango':15, 'lemon':5, 'coconut':15}

    count = [1,1,1,1,1]
    profit = []
    totalProfit = 0

    #atleast one tree of all
    for fruit in l.keys() :
        fruitprofit = (d//days[fruit])*l[fruit]
        profit.append(fruitprofit)
        totalProfit += fruitprofit

    useDays -= 5

    maxQty = n*0.4 - 1  #appeared once so max-1

    max1 = max(profit)
    profit.remove(max1)
    max2 = max(profit)
    profit.remove(max2)
    max3 = max(profit)

    for i in range(useDays) :
        if i<maxQty :
            totalProfit += max1
        elif i<maxQty*2 :
            totalProfit += max2
        elif i<maxQty*3 :
            totalProfit += max2

    f2.write(str(totalProfit))
    f2.write("\n")
    
f.close()
f2.close()