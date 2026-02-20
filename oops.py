# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("marks:", self.marks)
    
#     def show_grade(self):
#         if self.marks >= 90:
#             print("Grade: A")
#         elif self.marks >= 80:
#             print("Grade: B")
#         elif self.marks >= 70:
#             print("Grade: C")
#         elif self.marks >= 60:
#             print("Grade: D")
#         else:
#             print("Grade: F")

# name = input("Enter student name: ")
# marks = int(input("Enter student marks: "))
# s1 = student(name, marks)
# s1.display()
# s1.show_grade()

class Temperature:
    def __init__(self, celsius=None):
            self.celsius = float(input("Enter temperature in Celsius: "))

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

t = Temperature()  
print("Temperature in Fahrenheit:", t.to_fahrenheit())

# encapsulation: hiding the internal details of an object and only exposing a public interface. In Python, we can use private attributes (prefixing with __) to achieve encapsulation.
