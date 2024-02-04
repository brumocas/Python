# TODO
# Luhn’s Algorithm
def validation_card(card_number):
    length = len(card_number)
    sum = 0

    # First step
    for i in range(length - 1, 0, -2):
        n = 2 * int(card_number[i - 1])
        n = n % 10 + (n // 10)
        sum += n

    # Second step
    for i in range(length - 1, -1, -2):
        sum += int(card_number[i])

    # Third step
    if sum % 10 == 0:
        return True
    return False


def card_type(card_number):
    digit1 = int(card_number[0])
    digit2 = int(card_number[1])

    if digit1 == 4:
        return "VISA"

    if digit1 == 3 and (digit2 == 4 or digit2 == 7):
        return "AMEX"

    if digit1 == 5 and (1 <= digit2 <= 5):
        return "MASTERCARD"

    return "INVALID"


def main():
    card_number = input("Please input the card digits:\n")

    if not (len(card_number) == 16 or len(card_number) == 13 or len(card_number) == 15):
        print("INVALID")
        return

    # Checking if the card is legitimate
    if validation_card(card_number):
        # Checking card type
        print(card_type(card_number))
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
    

"""
Run your program as python credit.py, and wait for a prompt for input. Type in 378282246310005 and press enter. Your program should output AMEX.
Run your program as python credit.py, and wait for a prompt for input. Type in 371449635398431 and press enter. Your program should output AMEX.
Run your program as python credit.py, and wait for a prompt for input. Type in 5555555555554444 and press enter. Your program should output MASTERCARD.
Run your program as python credit.py, and wait for a prompt for input. Type in 5105105105105100 and press enter. Your program should output MASTERCARD.
Run your program as python credit.py, and wait for a prompt for input. Type in 4111111111111111 and press enter. Your program should output VISA.
Run your program as python credit.py, and wait for a prompt for input. Type in 4012888888881881 and press enter. Your program should output VISA.
Run your program as python credit.py, and wait for a prompt for input. Type in 1234567890 and press enter. Your program should output INVALID
"""