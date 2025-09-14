import random
arr=[]
for i in range(1,101):
    arr.append("Q"+str(i))
def selection_with_replacement(count):
    selection=[]
    for i in range(5):
        x=random.randint(1,100)
        selection.append(x)
        count[x-1]+=1
    return selection, count

def selection_without_replacement(count):
    selection=[]
    while len(selection)<6:
        x=random.randint(1,100)
        if x in selection:
            continue
        else:
            selection.append(x)
            count[x-1]+=1
    return selection, count

def simulate_test_with_replacement():
    tests=[]
    test_count=[0]*100
    for i in range(10000):
        test,test_count=selection_with_replacement(test_count)
        tests.append(test)
    return tests, test_count

def simulate_test_without_replacement():
    tests=[]
    test_count=[0]*100
    for i in range(10000):
        test,test_count=selection_without_replacement(test_count)
        tests.append(test)
    return tests, test_count

def unique_avg(test):
    sum=0
    for i in range(5):
        if test.count(i)>1:
            continue
        else:
            sum+=1
    return sum


test1,count1=simulate_test_with_replacement()
test2,count2=simulate_test_without_replacement()

num_uniques_with_replacement=[]
for i in test1:
    num_uniques_with_replacement.append(unique_avg(i))
Expected_with_replacement=sum(num_uniques_with_replacement)/len(test1)

num_uniques_without_replacement=[]
for i in test2:
    num_uniques_without_replacement.append(unique_avg(i))
Expected_without_replacement=sum(num_uniques_without_replacement)/len(test2)

def conditional_probability_Q2_given_Q1(tests):
    count_Q1 = 0
    count_Q1_and_Q2 = 0
    for t in tests:
        if 1 in t:   # Q1 is selected
            count_Q1 += 1
            if 2 in t:   # Q2 also selected
                count_Q1_and_Q2 += 1
    if count_Q1 == 0:
        return 0
    return count_Q1_and_Q2 / count_Q1

p_with = conditional_probability_Q2_given_Q1(test1)
p_without = conditional_probability_Q2_given_Q1(test2)