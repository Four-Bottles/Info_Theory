
import math

def InXueHao():      #输入学号
    a = input("请输入你的学号：")
    return str(a)


def ceil(x):       #对数字向上取整
    a = x - int(x)
    if a==0:
        return x
    else:
        return int(x)+1

#编码（返回编码的值）
    
def coding(string):       
    answer = ""
    Strlen = len(string)  #输入的位数
    div = 10       #码元数
    dLen = 0       #区间长度
    leftEnd = 0    #区间左端点
    rightEnd = 1   #区间右端点
    codingLen = ceil(float(math.log(math.pow(10, Strlen))) / math.log(2))  #编码长度
    
    for i in string:        #确定最后的区间
        index = int(i)
        dLen = float(rightEnd-leftEnd) / div
        leftEnd += (dLen*index)
        rightEnd =leftEnd + dLen

    end = float(leftEnd*0.01 + rightEnd*0.99) *2    #在区间内随机取一个实数，尽量靠近右界
    for i in range(codingLen):         #编码，即转换为二进制的数字（小数的转换形式）
        if end<float(1):
            answer += "0"
            end *= 2
        else:
            answer += "1"
            end -= float(1)
            end *= 2
    return answer

#译码（返回译码的值）

def getNumber(answer, length):    #第一个参数是编码符号，第二个参数是信源符号（学号）的长度
    leftEnd  = 0
    rightEnd = 1
    div = 10
    dLen = 0.1
    number = float(0)
    Id = ""
    wei = 0.5
    for i in answer:     #把编码转换为十进制的数（小数的转换形式）
        number += int(i)* wei
        wei *= 0.5
    for i in range(length):           #译码，分别对每一位进行搜索，满足区间的将其译码，直到位数长度还原一致
        rightEnd = leftEnd + dLen
        for j in range(div):
            if leftEnd<number and number<rightEnd:
                string = str(j)
                Id += string
                break
            else:
                leftEnd += dLen
                rightEnd += dLen
        dLen *= 0.1
    return Id

def show():
    a = InXueHao()
    code = coding(a)
    number = getNumber(code, len(a))
    print ("编码：",code)
    print ("码的个数：", len(code))
    print ("译码：", number)

show()
input("Press <enter>")
