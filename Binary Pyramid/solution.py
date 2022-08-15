row = 5
x = "01"
for i in range(row):
    i+=1
    if i == row:
        for k in range(i):
            k = k+1
            mystr = x*k
            print(mystr[1:])