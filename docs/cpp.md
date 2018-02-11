# C++ Concepts

## Templates
- Allow function and classes to have generic type. This allows a function or a class to work on many different data types without being rewritten for each one.

```
template <class identifier> function_declaration;
template <typename identifier> function_declaration;
```

```
template <class myType>
myType GetMax <myType a, myType b> {
    return (a > b ? a:b)
}
// Call this function
k = GetMax<int>(i, j);
```

## Abstract Classes
- An abstract class is, conceptually, a class that cannot be instantiated.
- Implemented as a class that has one or more pure virtual (abstract) functions.
- Intended to be inherited from by concrete classes.

## Virtual Functions
- Without *virtual* you get early binding. In the case of inheritance, which implementation of the method is used gets decided at compile time.
- With *virtual* you get late binding, which implementation of the method gets decided at run time.

### Virtual Destructors
- Allows deleting a derived class object using a pointer to a base class (otherwise results to undefined behaviour)
- Making the base class destructor virtual guarantees that the object of the derived class is destructed properly.

### Virtual Base Class
- Used in virtual inheritance, a way of preventing multiple instances of a given class appearing in an inheritance hierarchy.

```
class A { public: void Foo() {} };
class B : public A {};
class C : public A {};
class D : public B, public C {};
```

```
  A
 / \
B   C
 \ /
  D
```
```
D d;
d.Foo(); // is this B's Foo() or C's Foo() ??
```

```
class A { public: void Foo() {} };
class B : public virtual A {};
class C : public virtual A {};
class D : public B, public C {};
```
This means that there is only one ``instance`` of A included in the hierarchy.

```
D d;
d.Foo(); // no longer ambiguous
```

## Pointer vs Reference
A variable which stores the address of another variable is called a pointer.
1. A pointer can be reassigned, a reference cannot and must be assigned at initialization.
2. A pointer has its own memory address and size on the stack (4 bytes on x86) whereas a reference shares the same memory address as the original variable. Can think of reference as another name for that variable.
3. You can have pointers to pointers to pointers offering levels of indirection. Whereas references only offer one level of indirection.
4. Pointers can be assigned *nullptr* directly, reference cannot.
5. A pointer needs to be dereferenced with * to access the memory location it points to whereas a reference can be used directly. A pointer to a class/struct uses `->` to access its members whereas a reference uses `.`.
6. Finally think of reference as a constant pointer.

## Const pointers
- Read backwards
    - `int*` - point to int
    - `int const *` - pointer to constant int
    - `int * const` - const pointer to int
    - `int const * const` - const pointer to const int
    - `int ** const` - const pointer to a pointer to an int

- Examples
```
const int a = 10;
const int* ptr = &a;
*ptr = 5 // WRONG

```
```
int a = 10;
int* const ptr = &a;
*ptr = 5 // OK

```

## Dereference operator (*)
- When you want to access the value in the memory that the pointer points to
then you *dereference* the pointer.
- The operator itself can be read as ``value pointed to by``.

## Address-of Operator (&)
- The address of a variable can be obtained by preceding the name of a variable
with an ampersand sign (&).
- & is the address-of operator, and can be read simply as "address of"

## Mutable
- Used to allow a particular data member of const object to be modified.
- So marking specific attribute as modifiable from within `const`.

## C++ inline functions
- An optimization technique used by the compilers to reduce the execution time
- Functions can be instructed to compiler to make them inline so that compiler can
replace those function definition wherever those are being called.
- Compiler replaces the definition of inline functions at compile time instead of referring
function definition at runtime.
- This is just a suggestion to compiler to make the function inline, request may be ignored.

## Static member variables
- Static variables keep their values and are not destroyed even after they go out of scope.
- When we instantiate a class object, each object gets its own copy of all normal member variables.
- Unlike normal member variables, static member variables are shared by all objects of the class.
- Although you can access static members through objects of the class, it turns out that static members
exist even if no objects of the class have been instantiated!
- Think of static members as belonging to the class itself, not to the objects of the class.

## Static member functions
- If the static member variables are public, we can access them directly using the class name and
the scope resolution operator. But if the static member variables are private, static member functions
can be used to access that private member variable.



