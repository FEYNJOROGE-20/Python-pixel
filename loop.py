#for loop
for i in range (1,11):
    print(f"Welcome to my shop! customer {i} ")

    mycustomer=("Faith","Lavender","christine","Henry","Erick")

    for n in mycustomer:
        print(f"Welcome to my school {n}")
#suppose you buy
#bread ksh 130
#milk ksh 100
#sugar ksh 200
#blueband ksh 120
#calculate the total expense
   
my_shopping=[130,100,200,100]
total=0

for s in my_shopping:
    total=total+s
print(f"your total expense is {total}")

#while loop

num=0
while num <=8:
    print(f"loop :{num}")
num+=2

#imagine you start with 0 and save 100 everday until you save 500

money=0
while money <500:
   money=money+100
   print(f"Money  saved {money} ")

print("Congratulation!you reached your target")