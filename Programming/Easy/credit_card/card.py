#################################################################################
#   CTFLearn - Programming -> Credit Card Fraudster                             #
#   Difficulty: Easy                                                            #
#   Link: https://ctflearn.com/challenge/970                                    #
#   Synopsis:                                                                   #
#   I just arrested someone who is probably the most wanted credit card         #
#   fraudster in Europe. She is a smart cybercriminal, always a step ahead      #
#   INTERPOL and she kept unnoticed for years by never buying online, but       #
#   buying goods with a different card every time and in different stores. My   #
#   cyber-analysts found out after collecting all evidences she hacked into one #
#   the largest payment provider in Europe, reverse-engineered the software     #
#   present on the server and partly corrupted the card number validation code  #
#   to accept all her payments. The change enables acceptance of any            #
#   transaction with a card number multiple of 123457 and the Luhn check digit  #
#   is valid.                                                                   #
#                                                                               #
#   I caught her because every year she bought a bouquet of flowers next to the #
#   same cemetery. While handcuffing her at the flower shop's exit, she said    #
#   the flowers were for her lost father and today it is his death anniversary. #
#   She broke down in tears and she did some steps and threw something in the   #
#   sewers. My female colleague conducted a search on her, but she couldn't     #
#   find the card she used, only the receipt.                                   #
#                                                                               #
#   The little flower shop                                                      #
#   ======================                                                      #
#                                                                               #
#   European Express Debit                                                      #
#   Card Number: 543210******1234                                               #
#   SALE                                                                        #
#                                                                               #
#   Please debit my account                                                     #
#   Amount: 25.00€                                                              #
#   Can you help me to recover the card number so that I can confirm with the   #
#   flower merchant's bank the card number was used in that shop and is         #
#   fraudulent?                                                                 #
#                                                                               #
#   Hints:                                                                      #
#                                                                               #
#   1/ Luhn_algorithm                                                           #
#   2/ Flag format is CTFlearn{card_number}                                     #
#   Found Flag:                                                                 #
#           CTFlearn{5432103279251234}                                          #
#################################################################################
#   Output:
#   $ python card.py
#   Checking no: 5432100810111234
#   Valid: False
#   ---------------
#   Checking no: 5432102044681234
#   Valid: False
#   ---------------
#   Checking no: 5432103279251234
#   Valid: True
#   ---------------
#   Checking no: 5432104513821234
#   Valid: False
#   ---------------
#   Checking no: 5432105748391234
#   Valid: False
#   ---------------
#   Checking no: 5432106982961234
#   Valid: False
#   ---------------
#   Checking no: 5432108217531234
#   Valid: False
#   ---------------
#   Checking no: 5432109452101234
#   Valid: False
#   ---------------


def cardLuhnChecksumIsValid(card_number):
#    """ checks to make sure that the card passes a luhn mod-10 checksum """
#   Shamelessly stole from StackOverflow
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )


test = 1
first = "543210"
second = "1234"
cardno = ""
while test <= 999999:
     cardno = first + f'{test:06}' + second
     if (int(cardno) % 123457 == 0):
        print('Checking no: ' + cardno + '\n' + 'Valid: ' + str(cardLuhnChecksumIsValid(cardno)) + '\n' + '---------------')
     test +=1
     