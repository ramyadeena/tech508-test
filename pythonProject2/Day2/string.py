#include ' before and after the word.
word_string = "I said 'Wow!'"
print(word_string)

#include \ before and after the word.
second_string ='She said \'Wow!\''
print(second_string)

#include ''' before the word
third_string = '''He said 'Wow!'''
print(third_string)

##slice string
hw = "Hello World!"
print(hw)
# find out how many chanracters hw has?
print(len(hw)) #12
# Get the character in the first position in Hw
print(hw[0])
# Get the last character
print(hw[-1])
print(hw[11])
# Get the 2nd last character
print(hw[-2])

print(hw[2:1])
#it start at 2 and stop at 1 so it will show none on the output.

print(hw[-3:])
#it will give ld! as output which start from the end of the word and go back to 3characters.
print(hw[:5])
#it will print start from 0 and print upto 4 characters from beginning

# Starts from the second, stops at the fifth (doesn't include it)
print(hw[1:5])




