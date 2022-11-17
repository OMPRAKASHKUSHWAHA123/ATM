
# welcome section
print("****************************************")
print("***                                  ***")
print("***     Welcome to   Bank!!     ***")
print("***                                  ***")
print("****************************************")

# declearing pin
pi n =1234

# total number of chances to type pin if pin is error
chances =3
# Balance in account
balance = 5000
total_balance = 5000
# Mobile no. in the list(array(homogenious data))
mobile_nos = [9335210335, 9988776655, 4433221100]

# while loop work until chances=0 become
while chances != 0:

    # pin section
    user_pin = int(input("Please Enter Four Digit Pin:\n "))
    if user_pin != pin:
        chances -= 1
        print("Wrong pin number")
        print(f"You have {chances} chances left")
        if chances == 0:
            print("Your ATM card is block for 24 hour")
            exit()

    # menu section
    else:
        print("##########   Select option using uppercase  ##########")
        user_choice = input(''' 
                        -----------------------------
                        -----------------------------  
                          B:Balance inquiry
                          D:Deposite  
                          W:Cash Withdraw     
                          C:Change your PIN 
                          O:Other services
                        -----------------------------
                        -----------------------------
                          \n'''

                            )

        # balanbe inquery section
        if user_choice == "B":
            print(f"Your total balance is Rs. {balance}")

        # Deposite Section
        if user_choice == "D":
            deposit_user = int(input("Enter the amount that you will want to deposit :\n "))
            total_balance = deposit_user + balance
            balance = total_balance

            print(f"You have deposited Rs.{deposit_user} ")
            print(f"You total balance is Rs.{total_balance}")

        # Withdraw section
        if user_choice == "W":
            balance = total_balance
            withdraw_user = int(input("Enter the amount you want to withdraw:\n "))

            # condition ,user want to withdraw money
            if withdraw_user > balance:
                print("                SORRY \n                 ")
                print("Your Account have insufficient balance.")
                exit()
            else:

                total_balance = balance - withdraw_user
                print(f"You have withdrawn Rs.{withdraw_user}")
                print(f"Your total balance is Rs.{total_balance}")

        # pip change section
        if user_choice == "C":
            # type your old pin
            user_pin = int(input("Please Enter Your Four Digit Pin: "))

            if user_pin != pin:  # if old pin is wrong
                chances -= 1
                print("You type Wrong pin number")
                print(f"You have {chances} chances left")
                if chances == 0:
                    exit()
            else:  # if old pin is correct
                print("Enter your new PIN number:\n")
                new_pin = int(input())
                print("Enter your new PIN number again:\n")
                new_pin_again = int(input())

                # maching new_pin and new_pin_again
                if new_pin == new_pin_again:  # if both are same
                    print("Your new Pin is set!!!")


                # updating the pin
                def pins():  # function pin is define
                    global pin
                    pin = new_pin
                    return


                pins()  # pin function is calling

        # other services section
        if user_choice == "O":
            # new menu section
            print("!!! Select option using uppercase !!!")
            service = input("    M:Mobile top-up\n")

            if service == "M":
                # code for mobile section
                mobile_no = int(input("Enter your mobile no.\n"))

                if mobile_no in mobile_nos:
                    E_top = int(input("Enter amount you want to top-up:\n"))
                    # comparing balance and E_top money
                    if E_top > balance:
                        print("         :-(  SORRY   :-(        ")
                        print("  You have not enough balance.")
                        print("!!!!  Thankyou  for using our services !!!!!")
                        exit()
                    else:
                        balance = balance - E_top
                        print("Transaction successful.")
                        print("Thankyou for using our sevices")

                # if mobile number is wrong
                else:
                    print("This mobile no is not exist.")
                    exit()

    # exit section
    user_exit = input("Would You like to exit ?\n Y:Yes\n N:No\n ")
    if user_exit == "Y":
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!                                   !!!")
        print("!!!   Thankyou for using  Bank   !!!")
        print("!!!                                   !!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        exit()
    else:
        continue
