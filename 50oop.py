# single and multilevel
# class parent:
#     def func1(self):
#         print("parent class")
# class child(parent):
#     def func2(self):
#         print("child class")
# class ml(child):
#     def func3(self):
#         print("ml")
# object=ml()
# object.func1()
# object.func2()
# object.func3()




# hierarchical
# class parent:
#     def func1(self):
#         print("parent class")
# class child(parent):
#     def func2(self):
#         print("child class")
# class ml(parent):
#     def func3(self):
#         print("hierarchical")
# object=child()
# object.func1()
# object.func2()
# object=ml()
# object.func1()
# object.func3()

# multiple inheritance
# class parent:
#     def func1(self):
#         print("parent class")
# class child(parent):
#     def func2(self):
#         print("child class")
# class ml(child,parent):
#     def func3(self):
#         print("multiple")
# object=ml()
# object.func1()
# object.func2()
# object.fun

# class swift:
#     boot=150
#     cl="black"
#     def

class Bird:
    def intro(self):
        print("There are many types of birds.")


    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()

obj_ost.flight()


