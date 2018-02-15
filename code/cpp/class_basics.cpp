
// Class syntax
class MyClass {
    private:
        double var;
    public:
        MyClass(double v) {var = v;}
        ~MyClass() {};
        double Update(double v);
};
double Complex::Update(double v) {
    var =  v; return v;
}


// Data abstraction
class Stack
{

    public:
        virtual void push(int)=0;
        virtual int pop()=0;
};

class MyStack:public Stack
{
    private:
        int data_array[];

    public:
        void push(int){
            // Implement push op
        }

        int pop(){
            // Implement pop op
        }
};

// Copy constructor
class SampleClass
{
    public:
        int* ptr;
        SampleClass();

        // Copy constructor declaration
        SampleClass(SampleClass &obj);
};

SampleClass::SampleClass(){
    ptr = new int();
    *ptr = 5;
}

SampleClass::SampleClass(SampleClass &obj){
    // Create a new object
    ptr = new int();
    // Manually assign the value
    *ptr = *(obj.ptr);
    cout<<"Copy constructor... \n";
}

// overloading class constructors
#include <iostream>
using namespace std;

class Rectangle {
    int width, height;

public:
    Rectangle();
    Rectangle(int, int);
    int area (void) {return (width*height);}

};

Rectangle::Rectangle(){
    width = 5;
    height = 5;
}

Rectangle::Rectangle(int a, int b) {
    width = a;
    height = b;
}

int main() {
    Rectangle rect (3, 4);
    Rectangle rectb;
    cout << "rect area: "<< rect.area() << endl;
    cout << "rect area: "<< rectb.area() << endl;
    return 0;
}
