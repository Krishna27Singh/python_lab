import package1.circle as circle
import package1.rectangle as rectangle

radius = int(input("Enter the radius of circle"))

print(f"The area of circle is: {circle.area_of_circle(radius)}")
print(f"The circumference of circle is: {circle.circumference_of_circle(radius)}")

length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of the rectangle"))
print(f"The area of rectangle is: {rectangle.area_of_rectangle(length, breadth)}")
print(f"The perimiter of rectangle is: {rectangle.perimiter_of_rectangle(length, breadth)}")