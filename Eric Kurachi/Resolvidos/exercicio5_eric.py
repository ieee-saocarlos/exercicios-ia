ate_19 = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
dezenas = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
centenas = 'hundred'
milhar = 'onethousand'
total = 0

for i in range(1,1000):
    u = i%10
    d = int(((i%100)-u) /10)
    c = int(((i%1000)-(d*10)-u) /100)
    print(c,d,u)

    if c == 0:
        if d == 0 or d == 1:                                            #the number is between c01 and c19
            total += len(ate_19[(d * 10) + u])
        else:                                                           #the number is between c20 and c99
            total += len(dezenas[d]) + len(ate_19[u])

    else:
        if i%100 == 0:
            total -= 3
        elif d == 0 or d == 1:                                            #the number is between c01 and c19
            total += len(ate_19[c]) + len(centenas) + len('and') + len(ate_19[(d * 10) + u])
        else:                                                           #the number is between c20 and c99
            total += len(ate_19[c]) + len(centenas) + len('and') + len(dezenas[d]) + len(ate_19[u])

print(total+len(milhar))
