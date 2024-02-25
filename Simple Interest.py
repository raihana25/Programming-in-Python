P=int(input("Enter the investment amount: "))
years=int(input("Enter the no: of years: "))
rate=int(input("Enter the rate as a %: "))
amt=P
print("Year \t Starting balance \t Interest \t Ending Balance")
for i in range(1,years+1):
    interest= amt*(rate/100)
    prev_amt=amt
    amt+=interest
    print(i ,"\t" ,prev_amt ,"\t" ,interest, "\t", amt)
    
print('Ending Balance=',amt)
print('Total interest',(amt-P))