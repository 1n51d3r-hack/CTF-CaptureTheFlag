abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


for i in range(1,26):
    output = ''
    print 'ROT' + str(i) + '\n'

    infile = open('caesar_input.txt', 'r')

    for line in infile:
        for char in line:

                if char in ABC:
                    ind = ABC.index(char)
                    output = output + ABC[(ind-i)%26]

                elif char in abc:
                    ind = abc.index(char)
                    output = output + abc[(ind-i)%26]

                else:
                    output = output + char

    output = output + '\n\n'

    infile.close();

    print output + '\n\n'