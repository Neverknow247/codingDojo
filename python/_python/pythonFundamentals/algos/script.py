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



# function makeChangeWithDollars(cents) {
#     var coins = {
#         // "dollars": [100, 0],
#         // "half dollars": [50, 0],
#         "quarters": [25, 0],
#         "dimes": [10, 0],
#         "nickels": [5, 0],
#         "pennies": [1, 0]
#     }
#     for (key in coins) {
#         while (cents >= coins[key][0]) {
#             coins[key][1]++
#             cents -= coins[key][0]
#         }
#     }
#     console.log(cents + " cents can be represented by:")
#     for (key in coins) {
#         console.log(key + ": " + coins[key][1])
#     }
# }
# makeChangeWithDollars(297)

# class myCoins():
#     def __init__(self,q,d,n,p):
#         self.quarters = q
#         self.dimes = d
#         self.nickles = n
#         self.pennies = p
#     def coins(self):
#         print(f"Quarters: {self.quarters}, Dimes: {self.dimes}, Nickles: {self.nickles}, Pennies: {self.pennies}")
#         return self


# def change(cents):
#     q = 0
#     d = 0
#     n = 0
#     p = 0
#     coins = {
#     "quarters": [25, 0],
#     "dimes": [10, 0],
#     "nickels": [5, 0],
#     "pennies": [1, 0]
#     }
#     for key in coins:
#         while cents >= coins[key][0]:
#             coins[key][1]+=1
#             cents -= coins[key][0]
#             for i in range(4):
#                 if i == 0:
#                     q =(coins[key][1])
#                 if i == 0:
#                     d =(coins[key][1])
#                 if i == 0:
#                     n =(coins[key][1])
#                 if i == 0:
#                     p =(coins[key][1])
#     _change = myCoins(q,d,n,p)
#     return _change
# _change = change(41)
# _change.coins()





class myCoins():
    def __init__(self,q,d,n,p):
        self.quarters = q
        self.dimes = d
        self.nickels = n
        self.pennies = p
    def coins(self):
        print(f"Quarters: {self.quarters}, Dimes: {self.dimes}, Nickles: {self.nickels}, Pennies: {self.pennies}")
        return self

def change(cents):
    coins = {
    "quarters": [25, 0],
    "dimes": [10, 0],
    "nickels": [5, 0],
    "pennies": [1, 0]
    }
    for key in coins:
        while cents >= coins[key][0]:
            coins[key][1]+=1
            cents -= coins[key][0]
    return myCoins(coins["quarters"][1],coins["dimes"][1],coins["nickels"][1],coins["pennies"][1])
_change = change(42)
_change.coins()





# class Node:
#     def __init__(self,value_input):
#         self.value = value_input
#         self.next = None
#     def 

# class SLL():
#     def __init__(self):
#         self.head = None

#     def addToBack(self, value_input):
#         newnode = Node(value_input)
#         if self.head == None:
#             self.head = newnode
#         else:
#             runner = self.head
#             while runner.next != None:
#                 runner = runner.next
#             runner.next = newnode
#         return self
#     def display(self):
#         runner = self.head
#         result = ""
#         while runner != None:
#             result += f"{runner.value}-->"



class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.previous = None

    def addToBack(self, valueInput):
        newnode = Node(valueInput)
        if self.head == None:    
            self.head = newnode
        else:
            runner = self.head

            while runner.next != None:
                runner = runner.next

            runner.next = newnode
        return self

    def display(self):
        runner = self.head
        result = ""
        while runner != None:
            result += f"{runner.value}-->"
            runner = runner.next
        print(result)
        return self
    
    def addToFront(self, valueInput):
        if self.head != None:
            newnode = Node(valueInput)
            newnode.next = self.head
            self.head = newnode
            return self

    def contains(self, valueInput):
        runner = self.head
        while runner != None:
            if runner.value == valueInput:
                return True
            runner = runner.next
        return False

    def removeFront(self):
        if self.head != None:
            self.head = self.head.next
        return self

    def removeTail(self):
        if self.head == None:
            return "List must contain values"
        elif self.head.next == None:
            self.head = None
            return self
        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        runner.next = None
        return self

sll1 = SLL()
print(sll1.removeTail())

sll1.addToBack(5).removeTail().addToBack(8).addToBack(10).addToBack(20).display()
sll1.addToFront(69).addToFront(42).display()
sll1.addToBack(2).addToFront(1).addToBack(9).display()
sll1.contains(42)
sll1.removeFront().removeFront().display()
sll1.removeTail().display()






# n1 = Node(5)
# n2 = Node(8)
# n3 = Node(10)

# head = n1

# n1.next = n2
# n2.next = n3