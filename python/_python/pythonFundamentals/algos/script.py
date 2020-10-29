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




def book(_list):
    newList = ""
    for i in range (len(_list)):
        if _list[i] != _list[len(_list)-1]:
            if _list[i]+1 != _list[i+1] & _list[i]-1 != _list[i-1]:
                newList += str(_list[i])
                if _list[i]+1 == _list[i+1]:
                    newList += "-"
        # newList += 
    return newList
print(book([1,2,13,14,15,37,38,70]))


# “ Parens Valid
# Create a function that, given an input string str, returns a boolean whether parentheses in str are valid. Valid sets of parentheses always open before they close, for example. For "Y(3(p)p(3)r)s", return true. Given "N(0(p)3", return false: not every parenthesis is closed. Given "N(0)t )0(k", return false, because the underlined ")" is premature: there is nothing open for it to close.”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks. 



def parensValid(_str):
    _open = 0
    _close = 0
    for i in range(len(_str)):
        if _str[i] == "(":
            _open +=1
        if _str[i] == ")":
            _close +=1
        if _close > _open:
            return False
    if _open == _close:
        return True
    else:
        return False

print(parensValid("()test()"))




# python code below!
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]


_arr = [8,1,5,3,2,0]
def bubble(_array):
    for _i in range(len(_array)):
        for i in range(1,len(_array)):
            if _array[i] < _array[i-1]:
                _array[i], _array[i-1] = _array[i-1], _array[i]
    return _array

print(bubble(_arr))