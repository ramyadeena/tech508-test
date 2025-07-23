story1 = {
    "start": "Once upon a time there lived a girl  Goldilock with her family in woods",
    "middle": "she went to the bear house ,ate bear food,sat on the chair and slept there ",
    "end":" Bear came and saw the girl, Goldilock wakeup , scream on seeing the bear and ran away from that place",

}

print(story1)
print(type(story1))
print(story1.values())
print(story1.keys())
story1["character"] = "Goldilock"
print(story1.keys(),story1.values())
print(story1)
print("The end. I hope you enjoyed the story about", story1['character'] + "!")
