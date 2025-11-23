# ai_module.py
class SubfieldsInAI:
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
        
        
class OddEven:
    def OddEven():
        num=int(input("enter the number to check odd or even"))
        if num%2==0:
            print(num,"is even number")
        else:
            print(num,"is odd number")

class  ElegiblityForMarriage:
    def Elegible():
        gender=str(input("enter your gender"))
        age=int(input("enter your age"))
        print("your gender:",gender)
        print("your age:",age)
        if age>= 18:
            print("your eligible for marriage🤣🤣")
        else:
            print("not eligible for marriage🙄🙄")
        
class FindPercent:
    @staticmethod
    def percentage():
        subject_list = ["Subject1", "Subject2", "Subject3", "Subject4", "Subject5"]
        subject_dict = {}

       
        for subject in subject_list:
            mark = int(input(f"Enter marks for {subject}: "))
            subject_dict[subject] = mark

        
        for subject, mark in subject_dict.items():
            print(f"{subject} = {mark}")

        
        average = sum(subject_dict.values()) / len(subject_dict)
        print(f"Percentage: {average:.2f}")
 

class triangle:
    def triangle():
        Height1=int(input("enter the value of height"))
        Height2=int(input("enter the value of height"))
        Breadth=int(input("enter the value of Breadth"))
        Area=(Height1*Breadth)/2 
        Perimeter= Height1+Height2+Breadth
        print("Area of Triangle:",Area)
        print("Perimeter of Triangle:",Perimeter)
        


































































































































































        
        





        
        