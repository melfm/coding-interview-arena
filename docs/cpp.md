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

## Virtual Functions
- Without *virtual* you get early binding. In the case of inheritance, which implementation of the method is used gets decided at compile time.
- With *virtual* you get late binding, which implementation of the method gets decided at run time.

### Virtual Destructors
- Allows deleting a derived class object using a pointer to a base class (otherwise results to undefined behaviour)
- Making the base class destructor virtual guarantees that the object of the derived class is destructed properly.

## Pointer vs Reference
1. A pointer can be reassigned, a reference cannot and must be assigned at initialization.
2. A pointer has its own memory address and size on the stack (4 bytes on x86) whereas a reference shares the same memory address as the original variable. Can think of reference as another name for that variable.
3. You can have pointers to pointers to pointers offering levels of indirection. Whereas references only offer one level of indirection.
4. Pointers can be assigned *nullptr* directly, reference cannot.
5. A pointer needs to be dereferenced with * to access the memory location it points to whereas a reference can be used directly. A pointer to a class/struct uses `->` to access its members whereas a reference uses `.`.
6. Finally think of reference as a constant pointer.

## Const


## Mutable
- Used to allow a particular data member of const object to be modified.



