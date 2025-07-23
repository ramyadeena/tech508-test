str_with_extra_spaces = "   extra spaces at the start and end   "
print(len(str_with_extra_spaces))
#strip method removes extra space on the start and end of the string.
print(len(str_with_extra_spaces.strip()))

example_text = "Here's some text with some words of text"
#count method counts the number of time the text appear on the string.
print(example_text.count("text"))
exa_text =" The cat was chasing the mouse ,mouse hid under the bed, but cat found the mouse"
print(exa_text.count("mouse"))
print(exa_text.count("cat"))

# convert example1_text to lowercase & print it to the screen
example1_text = "HELLO WORLD"
print(example1_text.lower())

# convert example_text to uppercase & print it to the screen
example_text = "Here's some text with some words of text"
print(example_text.upper())

# capitalise the first letter in example_text & print it to the screen
word="ramya"
print(word.capitalize())

# replace the word 'with' in example_text with a comma (,) instead & print it to the screen
example_text = "Here's some text with some words of text"
print(example_text.replace('with',','))

x = 2

y = 5.4

z = " there's now a number 25.4 unless we put a space in!"

print(str(x)+str(y)+z)
#problem: we cannot add integer and string together( int and float can be added)
#so we should change all the integer to string and add for the final output which was asked