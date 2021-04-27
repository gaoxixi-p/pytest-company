###从控制(台输入数据，然后数据从小到大输出
# m = []
# for i in range(5):
#     x = int(input('please xie date:\n'))
#     m.append(x)
# m.sort()
# print(m)
####用*号输入字母2的图案
# print ('@'*8 )
# for i in range(3):
#     print ('       *')
# print ('@' * 8)
# for j in range(3):
#     print('*')
# print ('@'*8)
#####
# m=0
# for i  in range(100,201):
#     if i%2!=0:
#         m+=1
#         print(i)
# print('共计素数是：%d'%m)

# for n in range(100,1001):
#     i = n / 100
#     j = n / 10 % 10
#     k = n % 10
#     if i * 100 + j * 10 + k == i + j ** 3 + k ** 3:
#         print ('%d' % n)
#一 for循环  字符串格式输出
# for x in range(1,4):
#     for y in range(1,x+1):
#         print('{}*{}={}\t'.format(y,x,x*y),end='')
#     print("")
#二 函数：带参数
# def myfu(food):
#     for i in food:
#         print(i)
# fruit= ["apple", "banana", "cherry"]
# myfu(fruit)
####
# class TestCase():
#     def __init__(self):
#         pass
#     def lianx1(self):
#         self.lianx1="a"
#         return "nihao"
# if __name__ == '__main__':
#     test = TestCase()
#     print(test.lianx1())
####时间标准库
# import time
# print(time.asctime())
# print(time.localtime())
# print(time.time())
# print(time.strftime('%Y年%m月%d日 %H时%M分%S秒',time.localtime()))
###OS
import os
print(os.path.abspath("bonus.py"))