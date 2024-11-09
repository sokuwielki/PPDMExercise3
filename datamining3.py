import random
#We have n people
n=10_000_000
agents = [0]*n
#Only one of them is informed, quote "Initially, a designated agent has a piece of information"
starts_informed = random.randint(0, n - 1)
#We denote who's informed by 1 and uninformed by 0
agents[starts_informed] = 1
#Exercise expects THREE DIFFERENT SIMULATIONS
#So divide them in 3
protocol = "pushpull"
round = 0
#HERE CHANGE THE NAME OF THE FILE
with open("pushpull10_000_000.txt", "a") as file:    
## pull part
    if protocol == "pull":
        file.write(f"Simulating {protocol};\n")
        while sum(agents) != len(agents):
            round += 1
            for x in range(len(agents)):
                if agents[x] == 0:
                    if agents[random.randint(0, n-1)] == 1:
                        agents[x] = 1
            print(f"Round:{round} Informed:{sum(agents)}")
            file.write(f"Round:{round} Informed:{sum(agents)}\n")
    ## push part
    elif protocol == "push":
        file.write(f"Simulating {protocol};\n")
        while sum(agents) != len(agents):
            round += 1
            for x in range(len(agents)):
                if agents[x] == 1:
                    agents[random.randint(0, n-1)] = 1
            print(f"Round:{round} Informed:{sum(agents)}")
            file.write(f"Round:{round} Informed:{sum(agents)}\n")
    ## push and pull part
    elif protocol == "pushpull":
        file.write(f"Simulating {protocol};\n")
        while sum(agents) != len(agents):
            round += 1
            for x in range(len(agents)):
                if agents[x] == 1:
                    agents[random.randint(0, n-1)] = 1
                if agents[x] == 0:
                    if agents[random.randint(0, n-1)] == 1:
                        agents[x] = 1
            print(f"Round:{round} Informed:{sum(agents)}")
            file.write(f"Round:{round} Informed:{sum(agents)}\n")
