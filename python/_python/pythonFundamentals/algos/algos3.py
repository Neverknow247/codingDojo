def recursion(string):
    returnList = []
    temp = ""
    x = {}
    for i in range(len(string)):
        temp += string[i]
        x["temp{0}".format(i)] = temp
        # returnList.append(x)
    print(x)
    for key, value in x.items():
        print(value)
        returnList.append(value)
    # returnList.append(temp)
    print(returnList)
    return returnList

recursion("abc")


























def recursion2(string, temp = "", i= 0):
    returnList = []
    if len(string) == i:
        return temp
    for i in range(len(string)):
        temp += string[i]
        returnList.append(temp)
        returnList.append(recursion2(string[0])+recursion2(i))
    print(returnList)
    return returnList

recursion2("abc")


def ios(strinput, sub = "", i= 0):
    if len(strinput) == i:
        return sub
    else:
        return ios(strinput, sub+strinput[i], i+1) + ios(strinput, sub, i+1)

print(ios("abc"))

be = ['a','b']
ce = ['c','d']
be += ce
print(be)


def strSubsets(str):
    if len(str) == 0:
        return [""]
    result = []
    arr = strSubsets(str[1:])
    for i in range(len(arr)):
        result.append(arr[i])
        result.append(str[0]+arr[i])
    return result