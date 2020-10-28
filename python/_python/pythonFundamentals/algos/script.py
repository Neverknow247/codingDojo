def reverse(str):
    return str[::-1]


txt = reverse("hello")

print(txt)

goats = ["leb", "to", 325, 44]
for i in goats:
    print(i)






def pal(_str):
    _str = _str.lower()
    for i in range (round(len(_str)/2)):
        if _str[i] != _str[len(_str)-1-i]:
            return False
    return True

print(pal("Rcecar"))


def pal1(_str):
    _str = _str.lower()
    _str = _str.replace(" ","")
    for i in range (round(len(_str)/2)):
        if _str[i] != _str[len(_str)-1-i]:
            return False
    return True

print(pal1("RaceCar"))



def pal2(_str):
    punc = {
        "space":" ",
        "exclaim":"!",
        "period":"."
    }
    for _key, value in punc.items():
        _str = _str.replace(value,"")
    _str = _str.lower()
    for i in range (round(len(_str)/2)):
        if _str[i] != _str[len(_str)-1-i]:
            return False
    return True

print(pal2("Race .!Car"))



def isPalNoPunc(s):
    s = s.lower()
    i = 0
    j = len(s) - 1
    punc = [" ", ".", ",", ";", ":", "'", "(", ")", "!"] # add whatever punctuation you don't want checked
    while i < j:
        while s[i] in punc:
            i+=1
        while s[j] in punc:
            j-=1
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

print(isPalNoPunc("Race Car!"))



punc = {
    "space":" ",
    "exclaime":"!"
}
for key, value in punc.items():
    print(value)



# Martin is writing his opus: a book of algorithm challenges, set as lyrics to a suite of a cappella fugues. Some of ‘those fugueing challenges’ are less popular than others, so he needs an index. Given a sorted array of pages where a term appears, produce an index string. Consecutive pages should form ranges separated by a hyphen. For [1,13,14,15,37,38,70], return string "1, 13-15, 37-38, 70". Take care to get all the commas and spaces correct: Martin is palpably particular (practically persnickety!) about patchy punctuation.”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks. 

def book(_List):
    newList = []
    
