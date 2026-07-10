import re

# \d indicates a [0-9] decimal
# \w alpha numeric chars
# \D non decimal chars
# \W non alphanumric chars !@#$%^&*()+=
# \s white space
# \S non white space

pattern = r"\d\d"
data = "i have 77 dogs and 88 cats"
print(re.search(pattern,data))

data = "My adhar number is 6071-4659-9803"
# pattern = r"\d{4}-\d{4}-\d{4}"
pattern = r"[0-9]{4}-[0-9]{4}-[0-9]{4}"
print(re.search(pattern,data))

data = "My phone number is +91 9539438918"
# pattern = r"\W[0-9]{2}\s[0-9]{10}"
pattern = r"\W[0-9]+\s[0-9]+"
# + repetition
print(re.search(pattern,data))

data = "My mail id is jWTEUI295908!@#$%^&*()_@gmail.com"
pattern = r"[a-z][a-zA-Z0-9!@#$%^&*()_]+@[A-Za-z]+.[a-z]+"
print(re.search(pattern,data))

data = "need to go https://www.google.com/ "
pattern = r"https+\D+[a-z]+.[a-z]+.[a-z]+\W"
print(re.search(pattern,data))


data = "my email addresses are  qWERT2345678901#$%^&*_()*^&%$##@yahoTomail.com , j45QWERT&*%$#@gmail.coinunion , mohan123@hmail.com , azeeQWERT@gmail.com,j45QWERT&*%$#@gmail.com"
pattern = r"[a-z][a-zA-z0-9#$%^&*()]+@[A-Za-z]+.[a-z]+"
z = re.findall(pattern,data)
print(z)

data = "my email address is mohan123@hmail.com"
pattern = r"([a-z][a-zA-z0-9#$%^&*()]+)@([A-Za-z]+).([a-z]+)"
z = re.search(pattern,data)
print(z.group(0))
print(z.group(1))
print(z.group(2))
print(z.group(3))

data = "i have 3 dogs"
pattern = r"dogs"
z = re.sub(pattern,"Cats",data)
print(z)