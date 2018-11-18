#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <string>
#include <list>

/***********************************************************************
 * Declaration/Definition of the base-class Shape *
 ***********************************************************************/

class Shape
{
private:
 float m_size1;
 float m_size2;

public:
 virtual void OutputArea() = 0;
 virtual void OutputPerimeter() = 0;
 virtual void OutputNumberCorners() = 0;
 void SetSize1(float size)
 {
 m_size1 = size;
 }
 void SetSize2(float size)
 {
 m_size2 = size;
 }
 float GetSize1()
 {
 return m_size1;
 }
 float GetSize2()
 {
 return m_size2;
 }

}; //...

/***********************************************************************
 * Declaration/Definition of the child-classes *
 ***********************************************************************/

class Rectangle : public Shape
{

public:
 Rectangle(float size1, float size2);
 virtual void OutputArea();
 virtual void OutputPerimeter();
 virtual void OutputNumberCorners();
};
Rectangle::Rectangle(float size1, float size2)
{
 SetSize1(size1);
 SetSize2(size2);
}
void Rectangle::OutputArea()
{
 std::cout<< "Area: "<<GetSize1() * GetSize2()<<"\n";
}
void Rectangle::OutputPerimeter()
{
 std::cout<<"Perimeter: "<<2 * (GetSize1() + GetSize2())<<"\n";
}
void Rectangle::OutputNumberCorners()
{
 std::cout<<"Corners: 4"<<"\n";
}
class Square : public Shape
{

public:
 Square(float size1);
 virtual void OutputArea();
 virtual void OutputPerimeter();
 virtual void OutputNumberCorners();
};
Square::Square(float size1)
{
 SetSize1(size1);
}
void Square::OutputArea()
{
 std::cout<< "Area: "<<GetSize1() * GetSize1()<<"\n";
}
void Square::OutputPerimeter()
{
 std::cout<< "Perimeter: "<<4 * GetSize1()<<"\n";
}
void Square::OutputNumberCorners()
{
 std::cout<< "Corners: 4"<<"\n";
}
class Triangle : public Shape
{
public:
 Triangle(float size1, float size2);
 virtual void OutputArea();
 virtual void OutputPerimeter();
 virtual void OutputNumberCorners();
};
Triangle::Triangle(float size1, float size2)
{
 SetSize1(size1);
 SetSize2(size2);
}
void Triangle::OutputArea()
{
 std::cout<< "Area: "<<GetSize1() * GetSize2() / 2<<"\n";
}
void Triangle::OutputPerimeter()
{
 std::cout<< "Perimeter: "<<GetSize1() + GetSize2() + sqrt(pow(GetSize1(), 2) + pow(GetSize2(), 2))<<"\n";
}
void Triangle::OutputNumberCorners()
{
 std::cout<<"Corners: 3"<<"\n";
}
class Circle : public Shape
{
public:
 Circle(float size1);
 virtual void OutputArea();
 virtual void OutputPerimeter();
 virtual void OutputNumberCorners();
};
Circle::Circle(float size1)
{
 SetSize1(size1);
}
void Circle::OutputArea()
{
 std::cout<< "Area: "<<GetSize1() * GetSize1() * M_PI<<"\n";
}
void Circle::OutputPerimeter()
{
 std::cout<< "Perimeter: "<<2 * GetSize1() * M_PI<<"\n";
}
void Circle::OutputNumberCorners()
{
 std::cout<<"Corners: 0"<<"\n";
} // ...

/***************************************************************************
 * Main Function which is creating/reporting database (do not change!) *
 ***************************************************************************/

int main()
{

 //initialize an empty list of shapes
 std::list<Shape *> shapeDatabase;

 //interact with the user: ask the user to enter shapes one by one
 while (1)
 {
 //print instructions as to how to enter a shape
 std::cout << "Enter a type (Circle, Triangle, Square, or Rectangle) ";
 std::cout << "and one or two size parameters, ";
 std::cout << "separated with blank spaces:\n";

 float size1;
 float size2;

 //check which shape has been requested and store in the database
 std::string shapeType;
 std::cin >> shapeType;
 if (shapeType == std::string("Circle"))
 {
 std::cin >> size1;
 shapeDatabase.push_back(new Circle(size1));
 }
 else if (shapeType == std::string("Triangle"))
 {
 std::cin >> size1 >> size2;
 shapeDatabase.push_back(new Triangle(size1, size2));
 }
 else if (shapeType == std::string("Square"))
 {
 std::cin >> size1;
 shapeDatabase.push_back(new Square(size1));
 }
 else if (shapeType == std::string("Rectangle"))
 {
 std::cin >> size1 >> size2;
 shapeDatabase.push_back(new Rectangle(size1, size2));
 }
 else
 {
 std::cout << "Unrecognized shape!!\n";
 }

 //check if the user wants to add more shapes
 std::cout << "Do you want to add more shapes? (Enter Y or N)\n";
 std::string answer;
 std::cin >> answer;
 if (answer != std::string("Y"))
 break;
 }

 //iterate through the list and output the area, perimeter,
 //and number of corners of each entered shape
 std::list<Shape *>::iterator it = shapeDatabase.begin();
 int shapeCounter = 0;
 while (it != shapeDatabase.end())
 {
 std::cout << "Properties of shape " << shapeCounter++ << ":\n";
 (*it)->OutputArea();
 (*it)->OutputPerimeter();
 (*it)->OutputNumberCorners();
 it++;
 }

 return 0;
}