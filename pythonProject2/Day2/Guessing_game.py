# hint1: 5th and 6th letter
# hint2: last3 letter
# hint3:8th to 10th letter
# hint4: first two letters




original_word ="recommendation"
scrambled_word="eoommandretnic"

print("Here are some hints")
print("Scrambled word:" , scrambled_word)
print("Guess the original word from the scrambled version")

hint1= original_word[4:6] ## r-0 e-1,c-2,0-3m-4,m-5e-6
print(hint1)
hint2=original_word[-3:]
print(hint2)
hint3=original_word[7:10]
print(hint3)
hint4=original_word[0:2]
print(hint4)
hint5=original_word[2:5]
print(hint5)

print("What's your guess?")




