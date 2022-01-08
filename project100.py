class ATM : 
    def __init__(self , cardN , pin):
        self.c = cardN
        self.p = pin
        
    def checkBalance(self):
        print("The balance is $50,000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


   
def main():
    cardNumber = input("Insert your card num : ")
    
    pinNumber = input("Insert your pin num : ")

    user = ATM(cardNumber , pinNumber)

    print("Choose Your Activity - ")
    print("1- Balance Enquiry    2- Withdrawl")

    choice = int(input("Enter Your Choice [1 or 2] --> "))

    if (choice == 1):
        user.checkBalance()

    elif(choice == 2):
        amount = int(input("Enter the amount to be withdrawn"))
        user.withdrawl(amount)
    else:
        print("Enter a valid option")

main()