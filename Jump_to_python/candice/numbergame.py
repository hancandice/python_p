# numbergame

print("""
Dear Kom.

Guess a number that is between 0 and 1000.
Every time you input a bad answer, you need to start the game again.
You cannot finish this game unless you gave a good number.

I wish you good luck!

""")

secret_number = 573

answer_customer = int(input("What's the number you are thinking about ? : "))

while True:
    
    if answer_customer != secret_number:
        print("Oops! your answer is wrong. :/ ")
        if answer_customer > secret_number:
            answer_customer = int(input("Try again it's less! : "))
        else:
            answer_customer = int(input("Try again, its more ! : "))
    else :
        print("Congratulation! You got the right number!")
        break

    
