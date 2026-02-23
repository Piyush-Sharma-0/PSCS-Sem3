import random
import matplotlib.pyplot as plt

Q=[i for i in range(1,101)]
#0 for easy, 1 for hard
Difficulty=[0]*100
#assigning difficulty levels randomly
for _ in range(100):
    while Difficulty.count(1)<70:
        index=random.randint(0,99)
        Difficulty[index]=1

#SIMULATE QUESTION SELECTION
def select_with_replacement(x=5):
    selected=[]
    for _ in range(x):
        num=random.randint(1,100)
        selected.append(num)
    return selected

def select_without_replacement(x=5):
    selected=[]
    for _ in range(x):
        while True:
            num=random.randint(1,100)
            if num not in selected:
                selected.append(num)
                break
    return selected

def Test_simulation(simulations=10000, choice=None):
    Test=[]
    while choice not in [1,2]:
        choice=int(input("Enter 1 for selection with replacement, 2 for selection without replacement: "))    
    if choice==1:
        for _ in range(simulations):
            selected=select_with_replacement()
            Test.append(selected)
    elif choice==2:
        for _ in range(simulations):
            selected=select_without_replacement()
            Test.append(selected)
    else:
        print("Invalid choice")
    return Test


def count_frequency(Test):
    count=[0]*100
    for i in range(len(Test)):
        for j in Test[i]:
            count[j-1]+=1
    return count


def check_unique(test):
    unique=[]
    for i in test:
        if i not in unique:
            unique.append(i)
    return len(unique)

def average_unique(Test):
    avg_unique=0
    for i in range(len(Test)):
        avg_unique+=check_unique(Test[i])
    avg_unique/=len(Test)
    return avg_unique


def conditional_probablity(x=1,y=2):
    Test=Test_simulation(2)
    conditional_count=0
    for i in Test:
        if x in i and y in i:
            conditional_count+=1
    conditional_probablity=conditional_count/10000
    return  conditional_probablity

def easy_correct(Test=None):
    if Test is None:
        Test=Test_simulation(2)
    easy_correct=0
    correct=0
    for i in range(len(Test)):
        x=random.choice(Test[i])
        if Difficulty[x-1]==0:
            if random.random()<0.9:
                easy_correct+=1
                correct+=1
        else:
            if random.random()<0.4:
                correct+=1   
    probablity=easy_correct/correct
    theoretical_probablity=(0.9*0.3)/(0.9*0.3+0.4*0.7)
    if abs(probablity - theoretical_probablity) < 0.01:
        print("Simulated result matches theoretical result")
    return probablity

def distinct_per_group(x=10,y=1000,choice=2):
    while choice not in [1,2]:
        choice=int(input("Enter 1 for selection with replacement, 2 for selection without replacement: "))
    groups=[]
    unique=[]
    for _ in range(x):
        tests=Test_simulation(y,choice)
        groups.append(tests)
        unique.append(average_unique(tests))
    plt.boxplot(unique)
    plt.xlabel("Group")
    plt.ylabel("Average number of distinct questions")
    plt.title("Boxplot of Average Distinct Questions per Group")
    plt.show()

def co_selection_frequency(x=10000,choice=2):
    while choice not in [1,2]:
        choice=int(input("Enter 1 for selection with replacement, 2 for selection without replacement: "))
    co_matrix=[[0 for _ in range(100)] for _ in range(100)]
    tests=Test_simulation(x,choice)
    for test in tests:
        for i in range(len(test)):
            for j in range(len(test)):
                co_matrix[test[i]-1][test[j]-1]+=1
    plt.imshow(co_matrix, cmap='hot', interpolation='nearest')
    plt.colorbar(label="Co-selection frequency")
    plt.title(f"Heatmap of Question Co-selection Frequencies ({x} tests)")
    plt.xlabel("Question Index")
    plt.ylabel("Question Index")
    plt.show()

co_selection_frequency()

def biased_with_replacement(x=5):
    population = list(range(1, 101))
    weights = []
    for q in population:
        if 1 <= q <= 20:
            weights.append(2)
        else:
            weights.append(1)

    selected = random.choices(population, weights=weights, k=x)
    return selected

def biased_without_replacement(x=5):
    selected = []
    population = list(range(1, 101))
    weights = [2 if 1 <= q <= 20 else 1 for q in population]
    for _ in range(x):
        q = random.choices(population, weights=weights, k=1)[0]
        selected.append(q)
        idx = population.index(q)
        population.pop(idx)
        weights.pop(idx)
    return selected

distinct_per_group(10,1000,2)