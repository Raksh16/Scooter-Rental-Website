# def sumArray(arr,n):
#     if n==0:
#         return 0
#     elif n==1:
#         return arr[n-1]
#     else:
#         p=sumArray(arr,n-1) 
#         return arr[n-1] + p

	
# # Main
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# # print(sumArray(arr,n))
# def firstIndex(n,arr,x,si):
#     if n==0:
#         return -1
#     elif x==arr[si]:
#         return 0
#     else:
#         firstIndex(n,arr,x,si+1)

# # Main
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# si=0
# print(firstIndex(n,arr,x,si))


# def firstIndex(arr, x):
#     size = len(arr)
#     if size<=0:
#         return -1
#     if x == arr[0]:
#         return 0
#     smallAns = firstIndex(arr[1:],x)
#     if smallAns ==-1:
#         return -1
#     else:
#         return smallAns+1
    


# # Main
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# print(firstIndex(arr, x))

# def lastIndex(arr,x):
#     size = len(arr)
#     if size==0:
#         return -1
#     sl=arr[1:]
#     so=lastIndex(sl,x)
#     if so != -1:
#         return so+1
#     else:
#         if arr[0]==x:
#             return 0
#         else :
#             return -1



# # Main
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# print(lastIndex(arr,x))


# Problem: Remove x from string
# def removeX(string): 
#     if string[0]=='p' and string[1]=='i':
#         return -1
#     else:
#         return -2


# # Main
# string = input("Enter")
# print(removeX(string))


# def removeConsecutiveDuplicates(string):

#     if len(string)==0 or len(string)==1 :
#         return string
    
#     if string[0]==string[1]:
#         so=removeConsecutiveDuplicates(string[2:])
#         return string[1]+so
        
#     else:
#         so=removeConsecutiveDuplicates(string[1:])
#         return string[0]+so
            
    
# # Main
# string = input("enter").strip()
# print(removeConsecutiveDuplicates(string))


# def mergeSort(arr, start, end):
#     # Please add your code here
#     mid=(start+end)//2
#     s1=mergeSort(arr,start,mid-1)
#     s2=mergeSort(arr,mid,end)
#     merge(s1,s2,arr)
    
# def merge(s1,s2,arr):
#     s3=[]
#     if s1[0]<s2[0]:
#         arr=s1[0]
#         merge(s1[1:],s2,arr)
#         return arr
#     else:
#         arr=s2[0]
#         merge(s1,s2[1:],arr)
#         return arr
    
    

# # Main
# n=int(input("enter"))
# arr=list(int(i) for i in input("Enter").strip().split(' '))
# mergeSort(arr, 0, n)
# print(*arr)
# def mergeSort(arr, start, end):
#     # Please add your code here
#     mid=(start+end)//2

#     s1=mergeSort(arr,start,mid-1)
#     s2=mergeSort(arr,mid,end)
#     print(s1)
#     print(s2)
#     # merge(s1,s2,arr)
# # def merge(s1,s2,arr):
# #     if len(s1)==0 :
# #         arr=s2
# #         return arr
# #     elif len(s2)==0:
# #         arr=s1
# #         return arr
# #     if s1[0]<s2[0]:
# #         arr=s1[0]
# #         merge(s1[1:],s2,arr)
# #         return arr

# #     else:
# #         arr=s2[0]
# #         merge(s1,s2[1:],arr)
# #         return arr
# # Main
# n=int(input("enter n"))
# arr=list(int(i) for i in input("enter arr").strip().split(' '))
# mergeSort(arr, 0, n)
# # print(*arr)


# def quickSort(a, s, e):
#     # Please add your code here
#     if s>=e:
#         return
#     par=partition(a,s,e)
#     quickSort(a,s,par-1)
#     quickSort(a,par+1,e)
# def partition(a,si,ei):
#     c=0
#     for x in range(si+1,ei):
#         if a[si]>a[x]:
#             c=c+1
#     a[si],a[si+c]=a[si+c],a[si]
#     key=si+c
#     piv=a[si+c]
#     i=si
#     j=ei-1
#     while i<j:
#         if a[i]<piv:
#             i=i+1
#         elif a[j]>piv:
#             j=j-1
#         else:
#             a[i],a[j]=a[j],a[i]
#             i=i+1
#             j=j-1
#     return key 
        

# n=int(input("Enter n "))
# arr=list(int(i) for i in input("Enter arr  ").strip().split(' '))
# quickSort(arr, 0, n)
# print(*arr)


# def merge(a1,a2,arr):
#     i=0
#     j=0
#     k=0
#     while i<len(a1) and  j<len(a2) :
#         if a1[i]<a2[j]:
#             arr[k]=a1[i]
#             k=k+1
#             i=i+1
#         else:
#             arr[k]=a2[j]
#             k=k+1
#             j=j+1
#     while i<len(a1):
#         arr[k]=a1[i]
#         k=k+1
#         i=i+1
#     while j<len(a2):
#         arr[k]=a2[j]
#         k=k+1
#         j=j+1
# def mergeSort(arr):
#     if len(arr)== 0 or len(arr)==1:
#         return
#     mid=len(arr)//2
#     a1 =arr[0:mid]
#     a2 =arr[mid:]
#     mergeSort(a1)
#     mergeSort(a2)
#     merge(a1,a2,arr)

# # Main
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# mergeSort(arr)
# print(*arr)


# def towerofhanoi(n,a,b,c):
#     # Please add your code here
#     if n==1:
#         print("{} {}".format(a,c))

#     else:
#         towerofhanoi(n-1,a,c,b)
#         print("{} {}".format(a,b))
#         towerofhanoi(n-1,b,c,a)
#         print("{} {}".format(b,c))

# n=int(input("n"))
# towerofhanoi(n-1, 'a', 'b', 'c')


# def geo(n):
#     if n==0:
#         return 1
#     so=geo(n-1)
#     sum=so+(1/(pow(2,(n-1))))
#     return sum
# #Main
# n=int(input())
# print(geo(n+1))


# s=str(input("enter"))
# l=len(s)
# print(s[:l-1])
# def palan(s,s1):
#     if s==s1:
#         print("true")
#     else:
#         print("false")

# s=str(input())
# s1=s[::-1]
# palan(s,s1)


# number=int(input("Enter "))
# if (number == 0) {
#       return 1;
#     } else if (number <= 9) {
#       return 0;
#     } else {
#       return ((number % 10 == 0) ? 1 : 0) + zeroCount(number / 10);
#     }
#   }




# c=0
# while a>0:
#     s=a%10
#     if a==0:
#         c+=1
#         a=int(a/10)
#     else :
#         a=int(a/10)
# print(c)





# b=int(input("Enter "))
# sum=0
# for x in range(b):
#     x=a
#     sum+=x
# print(sum)






# while n>=1:
#     sum+=n%10
#     n=int(n/10)
# print(int(sum))


# def zero(n):
#     if n==0:
#         return 1
#     elif n%10==0:
#         c=zero(int(n/10))+1
#         return c
    	
#     else:
#         p=zero(int(n/10))
#         return p
        


# n=int(input("Enter"))
# print(zero(int(n)))

# def fun(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     so=int(n)%10
#     f=int(int(n)/10)
#     q=fun(str(f)) + str(so)
#     return q
# n=str(input())
# print(fun(n))

# n=str(input())
# p=int(n)
# print(p%10)


# def stringToInt(str):

#     if (len(str) == 1):
#         return ord(str[0]) - ord('0')

#     y = stringToInt(str[1:])
 

#     x = ord(str[0]) - ord('0')

#     x = x * (10**(len(str) - 1)) + y
#     return int(x)

# n=str(input())
# #print(fun(n))
# print(stringToInt(n))


# def star(s):
#     if len(s)==1:
#         return s
#     if s[0]==s[1]:
#         if s[1]==s[2]:
#             s=s[1]+'*'+star(s[1:])
#             return s
#         else:
#             s=s[0]+'*'+star(s[1:])
#     else:
#         p=s[0]+star(s[1:])
#         return p
    
# #MAIN
# s=str(input())
# print(star(s))



# def star(s):
#     if len(s)==1 or len(s)==0:
#         return s
#     so=star(s[1:])
#     if s[0]==so[0]:
#         s=s[0]+'*'+so    
#         return s
#     else :
#         return so
    

    
# #MAIN
# s=str(input())
# print(star(s))


def stz(s):
    if len(s)==0 or len(s)==1:
        return s
    elif s[0]=='a':
        so=stz(s[1:])
        if s[0]=='\0' or so[0]=='a':
            return 1
        elif so[0]=='b':
            if so[1]=='b' :
                if s[2]=='a' or s[2]=='\0':
                    return 1

    else:
         return -1

# #Main
# s=str(input())
# z=stz(s)
# if z==1:
#     print('true')
# else:
#     print('false')



#     def checkAB(string,sub):
# 	if len(string) == 0:
# 		return True

# 	if sub == 'a':
# 		if string[0] != sub:
# 			return False
# 		return checkAB(string[1:],'a') or checkAB(string[1:],'bb')
    
#     if len(string) < 2 or string[0:2] != sub:
#         return False
    
#     return checkAB(string[2:],'bb')
#     pass
    
# string=str(input())
# sub = 'a'
# result = checkAB(string,sub)
# if result:
#     print('true')
# else:
#     print('false')



# def checkAB(string,sub):
	# if len(string) == 0:
	# 	return True

	# if sub == 'a':
	# 	if string[0] != sub:
	# 		return False
	# 	return checkAB(string[1:],'a') or checkAB(string[1:],'bb')
	# if 
	# 	if string[0] != sub:
	# 		return False
	# 	return checkAB(string[1:],'a') or checkAB(string[1:],'bb')
    # if (len(string) < 2) or (string[0:2] != sub) :
    #     return False
    
    # return checkAB(string[2:],'bb')
    
# string=str(input())
# sub = 'a'
# result = checkAB(string,sub)
# if result:
#     print('true')
# else:
#     print('false')



# class Student:
#      name = “Rohan”
#      age = 16
# s1 = Student()
# s2 = Student()
# print(s1.name,end=” “)
# print(s2.name,end=” “)

# class Student:
#     pp = 50

# s1 = Student()
# s1.pp= 58
# s2 = Student()
# s2.pp = 60
# print(s1.pp)


# 

# 
# class Student:

#     def __init__(self,name,age):
#         self.name = "Rohan"
#         self.age = 20

#     def print_student_details():
#         print(self.name, end= " ")
#         print(self.age)


# s = Student("Priya",20)
# s.print_student_details()
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def print_student_details(self):
#         print(self.name, end= " ")
#         print(self.age)

# s = Student("Rohan",60)
# s.print_student_details()


# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def print_student_details():
#         print(self.name, end=" ")
#         print(self.age)

#     @staticmethod
#     def isTeen(age):
#         return age>16

# a = Student.isTeen(18)
# print(a)


# class Student:
#      def __init__(self,name,age):
#         self.__name = name
#         self.age = age
# def print_student_details():
#         print(self.__name, end= " ")
#         print(self.age)

# s = Student("Rohan",20)
# print(s.name)


# class Student:
#      def __init__(self,name,age):
#         self.__name = name
#         self.age = age
#      def print_student_details(self):
#         print(self.__name, end= " ")
#         print(self.age)
# s = Student("Rohan",20)
# s.print_student_details()


# class Vehicle:
#      def __init__(self,color):
#          self.color = color
# class Car(Vehicle):
#      def __init__(self,color,numGears):
#          self.numGears = numGears
# c= Car("black",5)
# print(c.color)

# class Vehicle:
#     def __init__(self,color):
#         self.color = color
# class Car(Vehicle):
#     def __init__(self,color,numGears):
#         super().__init__(color)
#         self.numGears = numGears
# c= Car("black",5)
# print(c.color)


# class Vehicle:
#      def __init__(self,color):
#          self.__color = color
# class Car(Vehicle):
#     def __init__(self,color,numGears):
#         super().__init__(color)
#         self.numGears = numGears
#     def printCar(self):
#         print(c.__color,end=" ")
#         print(c.numGears)
# c = Car("black",5)
# c.printCar()
# class Vehicle:
#     def __init__(self,color):
#         self.color = color
#     def print(self):
#         print(c.color,end=" ")
# class Car(Vehicle):
#     def __init__(self,color,numGears):
#         super().__init__(color)
#         self.numGears = numGears
#     def print(self):
#         self.print()
#         print(c.numGears)
# c = Car("black",5)
# c.print()

# def checkNumber(arr, x):
#     if len(arr)==0:
#         return "false"
#     elif arr[0]=='x':
#         return "true"
#     else :
#         checkNumber(arr[1:],x)
    
#     pass

# # Main
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# checkNumber(arr, x)

# def checkNumber(arr, x):
#     if len(arr)==0:
#         print("false")
#     elif arr[0]=='x':
#         print("true")
#     else :
#         print(checkNumber(arr[1:],x))
    

# # Main
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# checkNumber(arr, x)



# def checkNumber(arr, x):
#     if len(arr)==0:
#         return -1
#     elif arr[0]=='x':
#     	return 1
#     else :
#         s0=checkNumber(arr[1:],x)
#         return s0
    

# # Main
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# if checkNumber(arr, x)==1:
#     print("true")
# else :
#     print("false")



# def merge(arr,si,m,ei,size):
#     i=si
#     j=m+1
#     k=si
	
    
#     temp[size]
#     while(i<=m and j<=ei):
#         if  arr[i]<arr[j]:
#             temp[k]=arr[i]
#             i=i+1
#             k+=1
#         else:
#             temp[k]=arr[j]
#             j=j+1
#             k+=1
#     while(i<=m):
#         temp[k]=arr[i]
#         i=i+1
#         k+=1
#     while(j<=ei):
#     	temp[k]=arr[j]
#         j=j+1
#         k+=1
#     for x in range(si,ei):
#         arr[x]=temp[x]



# def checkAB(string,sub):
# 	if len(string) == 0:
# 		return True

# 	if sub == 'a':
# 		if string[0] != sub:
# 			return False
# 		return checkAB(string[1:],'a') or checkAB(string[1:],'bb')
#         if len(string) < 2 or string[0:2] != sub:
#         	return False
    
#         return checkAB(string[2:],'bb')

    
# string=str(input())
# sub = 'a'
# result = checkAB(string,sub)
# if result:
#     print('true')
# else:
#     print('false')










# 
# from abc import ABC,abstractmethod

# class A(ABC):

#     @abstractmethod
#     def fun1(self):
#         pass

#     @abstractmethod
#     def fun2(self):
#         pass

# class B(A):

#     def fun1(self):
#         print("funct1")
# o = B()
# o.fun1()


# from abc import ABC,abstractmethod

# class A(ABC):

#     @abstractmethod
#     def fun1(self):
#         print("fun A")

#     @abstractmethod
#     def fun2(self):
#         pass

# class B(A):
#     def fun1(self):
#         super().fun1()
#     def fun2(self):
#         print("fun2")
# o = B()
# o.fun1()
# try:
#     a = 10
#     b = 0
#     c = a/b
#     print(c)
# except ValueError:
#     print("Exception occured")


try:
    a = 10
    b = 0
    c = a/b
    print(c)
except :
    print("Exception occured")