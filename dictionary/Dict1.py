#Program to count the frequency of words in a string
s="Hello world! I welcome you all here, to greet you with Hello. How are you all? I am fine too. Bye world "

dct={}
s=s.translate({ord(i): None for i in '.,!:;\'/?'})
slist=s.split()

for word in slist:
    if (word in dct):
        dct[word]+=1
    else:
        dct[word]=1

print(dct)
