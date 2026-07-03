#Task-separate vowels and consonats in a string  "hi hello ravi garu"
l="hi hello ravi garu"
vowels=["a","e","i","o","u"]
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm','n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
spaces=" "
vow=[val for val in l if val in vowels]
space=[val for val in l if val ==" "]
con=[val for val in l if val in consonants ]
print(list(set(space)))
print(list(set(vow)))
print(list(set(con)))