#!/usr/bin/env python
# coding: utf-8

# In[47]:


import math
    
    
def main() :
    r = Rectangle(10, 5, 3)

    op = r.option()

    if op == 1 :
        area = r.getCube()
    else :
        area = r.setValue()
    
    print(area)



class Rectangle:
    def __init__(self, width = 1, high = 1, diagonal = 1):
        self.__width = width
        self.__high = high
        self.__diagonal = diagonal
        self.__option = 0
        
    def option(self) :
        if self.__width == self.__high == self.__diagonal :
            self.__option = 1
        else :
            self.__option = 2
        return self.__option

    
    def setValue(self) :
        return self.__width * self.__high * self.__diagonal
    
    
    def getCube(self):
        return self.__width * self.__width * self.__width
    
main()


# In[46]:


import random

def main() :
    list_answer = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']]
    print('질문에 대한 정답')
    print(list_answer[0])
    print(list_answer[1])
    print()
    
    list_student = []

    
    random_answer(list_student)
    
    print('질문에 대한 학생의 답')
    for i in range(8) :
        print(list_student[i])
        
    
    
    num = answer_num(list_answer, list_student)
    
    Result(num)


        
def random_answer(list_student) :
    for i in range(8) :
        list_student.append([chr(random.randint(65, 69)) for j in range(10)])
    return list_student


def answer_num(list_answer, list_student) :
    num_answer = []
    for i in range(8) :
        num = 0
        for r in range(10) :
            if list_answer[1][r] == list_student[i][r] :
                num += 1
        num_answer.append(num)           
    return num_answer
        
    
    
def Result(num) :
    for j in range(8) :
        print(j,'번 학생의 정답 문항의 개수는', num[j], '입니다.')

        
        
main()
    

    


# In[43]:


import random

def main() :
    RandomList = []

    
    CreateList(RandomList)
    print(RandomList[0])
    print(RandomList[1])
    
    
    print(Lamda(RandomList))



def CreateList(RandomList) :    
    for i in range(2) :
        RandomList.append([random.randint(0, 10) for j in range(10)])
    return RandomList
        
    
def Lamda(RandomList) :
    num_list = []
    for r in range(10) :
        num1 = RandomList[0][r] + RandomList[1][r]
        num2 = num1 / 2
        num_list.append(num2)
    return num_list
    

    
    
main()


# In[ ]:





# In[ ]:





# In[ ]:




