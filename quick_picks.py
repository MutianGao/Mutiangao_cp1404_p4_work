import random
Constants = []
times_input = int(input("How many quick picks? "))
for times_input in range(1, times_input+1):
    ran = random.sample(range(0, 46), 6)
    ran.sort()
    Constants.append(ran)
    print(ran)
print(Constants)