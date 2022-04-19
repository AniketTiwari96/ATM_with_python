print("plese wnter your card")
password=1234
pin=int(input("plese enter your pin"))
balance=5000
if pin==password:
	   print("""1==balance
	                2==withdraw_amount
	                3==deposite_amount
	                4==exit""")
option=int(input("plese enter your choice"))
if option==1:
	 print(f"your caurrent balance is {balance}/-")
elif option==2:
	 withdraw_amount=int(input("plese enter your withdraw_amount"))
	 balance=balance-withdraw_amount
	 print(f"{withdraw_amount}is debited from your account")
	 print(f"your updeted caurrent balance is{balance}")
elif option==3:
	 deposite_amount=int(input("plese enter deposite_amount"))
	 balance=balance+deposite_amount
	 print(f"{deposite_amount} is deposite from your amount")
	 print(f"your updeted caurrent balance is{balance}")
elif option==4:
     print("exit")
else:
	 print("plese enter the valid pin try again")
	          
