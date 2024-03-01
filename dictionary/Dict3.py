#Given two dictionaries say D1 and D2.Write a program to print all common keys in both D1 and D2
d1={"K1":"V1", "K2":"V2", "K3":"V3", "K4":"V4", "K5":"V5"}
d2={"K1":"V1","K5":"V5","K6":"V6","K3":"V3"}
for k,v in d1.items():
    if k in d2 : print(k,v)