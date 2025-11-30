outcomes = [1, 0, 1, 1, 0, 0, 1, 1]
c=0
for i in outcomes:
    if i==1:
        c+=1
EP=c/len(outcomes)
print(EP)
