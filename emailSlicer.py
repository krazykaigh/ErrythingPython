word = "supercalifragilisticexpialidocious"

# print(f"{}"[(word[5:10:2])])
sliceOfWord = (word[4:9:1])
print("{}".format(sliceOfWord))
# rcali

print("{}".format(word[5:12:1]))
# califra

print("{}".format(word[word.index("per"):word.index("ex")]))
# percalifragilistic

print("{}".format(word[word.index("per"):word.index("e")]))
# p

sliceOfWord = (word[::-1])
print("{}".format(sliceOfWord))