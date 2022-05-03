# How Slicers Work

from xml import dom


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

# here is a very long word

word = "antidisestablishmentarianism"

# use a slice to take out the word "establishment"
# and store it in the answer variable....

answer = word[word.index("e"):word.index("ari")]
print("{}".format(answer))

# ---------- Email Slicer Program --------------

# get user email address
email = input("Enter complete email address : ")

# slice out user name
userName = email[:email.index("@")]
print(f"User name = {userName}")

# slice domain name
domainName = email[(email.index("@")+1):]
print(f"Domain name = {domainName}")

# format message
output = "Your username is {0}, and your domain name is {1}".format(userName, domainName)


# display output message
print(output)


