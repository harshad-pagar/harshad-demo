print('''
1.deposite
2.withdraw
3.chek balance
4.exit
''')
pin=1234
choice=(int(input('enter a choice : ')))
userpin = (int(input("enter pin :")))
balance=5500


if pin==userpin:
    if choice==1:
        deposite=int(input("enter deposite amount"))
        if deposite > 0:
            balance += deposite
            print('deposite ',deposite,'new balace',balance)

        else:
            print('enter valid amount')


    elif choice==2:
        withdraw=int(input("enter withdraw amount"))
        if withdraw < balance:
             balance -= withdraw
             print('withdraw ',withdraw,'rb',balance)

        else:
             print('insufficient funds')


    elif choice==3:
        print('your balace is ',balance)


    elif choice==4:
        print("thank you for visiting me")
else:
    print("incorrect pin,try again")



