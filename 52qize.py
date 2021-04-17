class python:
    def python(self):
        nm=input("enter your name please")
        print("hello",nm,"welcome to Python Quize lets! begin all the best (:")
        s=0
        # question no.1
        print("Q1. Which is the correct operator for power(xy)?")
        print("1) X^y , 2) X**y , 3) X^^y , 4) None of the mentioned")
        a=int(input("Please enter correct option"))
        if(a==2):
            print("correct answer")
            s+=1
        else:
            print("sorry wrong answer")
            # pass
        #question no.2
        print("Q2. Which one of these is floor division?")
        print("1) // , 2) / , 3) % , 4) none of the mention")
        a = int(input("Please enter correct option"))
        if (a == 1):
            print("correct answer")
            s += 1
        else:
            print("sorry wrong answer")
        # question3
        print("Q3. What is the answer to this expression, 22 % 3 is?")
        print("1) 7 , 2) 1 , 3) 0 , 4) 5")
        a = int(input("Please enter correct option"))
        if (a == 2):
            print("correct answer")
            s += 1
        else:
            print("sorry wrong answer")
        # question 4
        print("Q4. Operators with the same precedence are evaluated in which manner?")
        print("1) Left to Right , 2) Right to Left , 3) Can’t say , 4)None of the mentioned")
        a = int(input("Please enter correct option"))
        if (a == 1):
            print("correct answer")
            s += 1
        else:
            print("sorry wrong answer")
        print("total correct answer",s,"out of 4")
class CPP:
    def cpp(self):
        nm = input("enter your name please")
        print("hello", nm, "welcome to C++ Quize lets! begin all the best (:")
        s = 0
        #question 1
        print("Q1  Which of the following is called address operator?")
        print("1) *, 2) & , 3) _, 4) %")
        a = int(input("Please enter correct option"))
        if (a == 2):
            print("correct answer")
            s += 1
        else:
            print("sorry wrong answer")
        #question 3
        print("Q2 Which of the following is used for comments in C++?")
        print("1)  // comment , 2)  /* comment */ , 3)  both // comment or /* comment */ , 4)// comment */")
        a = int(input("Please enter correct option"))
        if (a == 3):
            print("correct answer")
            s += 1
        else:
            print("sorry wrong answer")
        #Question 3
        print("Q3 Which of the following is the correct syntax of including a user defined header files in C++?")
        print("1)  #include <userdefined.h> , 2)#include <userdefined> ,3) #include “userdefined” , 4)#include [userdefined]")
        a = int(input("Please enter correct option"))
        if (a == 3):
            print("correct answer")
            s += 1
        else:
            print("sorry wrong answer")
        print("Q4 Which function is used to read a single character from the console in C++?")
        print("1) cin.get(ch) , 2) getline(ch) , 3) read(ch) , 4) scanf(ch)")
        a = int(input("Please enter correct option"))
        if (a == 1):
            print("correct answer")
            s += 1
        else:
            print("sorry wrong answer")
        print("total correct answer", s, "out of 4")
class html:
    def html(self):
        nm = input("enter your name please")
        print("hello", nm, "welcome to Html Quize lets! begin all the best (:")
        s = 0
        print("Q1. Which attribute specifies a unique alphanumeric identifier to be associated with an element?")
        print("1) class , 2)  id , 3) article , 4) html")
        a = int(input("Please enter correct option"))
        if (a == 2):
            print("correct answer")
            s += 1
        else:
            print("sorry wrong answer")
        # question 2
        print("Q2. Which attribute is used to provide an advisory text about an element or its contents?")
        print("1) tooltip , 2) dir , 3) title , 4) head")
        a = int(input("Please enter correct option"))
        if (a == 3):
            print("correct answer")
            s += 1
        else:
            print("sorry wrong answer")
        # question 3
        print("Q3 The __________ attribute sets the text direction as related to the lang attribute.")
        print("1) lang , 2)  sub , 3) dir , 4) ds")
        a = int(input("Please enter correct option"))
        if (a == 3):
            print("correct answer")
            s += 1
        else:
            print("sorry wrong answer")
        # question 4
        print("Q4 Which of the following is the attribute that is used to set a global identifier for a microdata item?")
        print("1)key , 2) id , 3) itemclass , 4) itemid")
        a = int(input("Please enter correct option"))
        if (a == 3):
            print("correct answer")
            s += 1
        else:
            print("sorry wrong answer")
        print("total correct   answer", s, "out of 4")
o1=python()
o2=CPP()
o3=html()

n=int(input("enter 1 for python quize , enter 2 for C++ Quize ,Enter 3 for Html Quize"))
if(n==1):
    o1.python()
elif(n==2):
    o2.cpp()
elif(n==3):
    o3.html()
else:
    print("invalid input")