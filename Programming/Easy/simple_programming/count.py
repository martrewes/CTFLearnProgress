#################################################################################
#   CTFLearn - Programming -> Simple Programming                                #
#   Difficulty: Easy                                                            #
#   Link: https://ctflearn.com/challenge/174                                    #
#   Synopsis:                                                                   #
#   Can you help me? I need to know how many lines there are where              #
#   the number of 0's is a multiple of 3 or the numbers of 1s is a              #
#   multiple of 2. Please! Here is the file:                                    #
#   https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys      #
#   Flag:                                                                       #
#           CTFlearn{6662}                                                      #
#################################################################################

numOnes = 0
numZeros = 0

with open('data.dat', 'r') as f:
    lines = f.readlines()
    for line in lines:
        zeros = line.count('0')
        ones = line.count('1')
        if (zeros % 3 == 0):
            numZeros +=1
        elif (ones % 2 == 0):
            numOnes +=1
        #print(str(zeros) + ' ' + str(ones))
            

print(str(numZeros) + ' ' + str(numOnes))
print(str(numOnes + numZeros))