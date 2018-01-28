# C++ Concepts

## Templates
- Allow function and classes to have generic type. This allows a function or a class to work on many different data types without being rewritten for each one.

```
template <**class** identifier> function_declaration;
template <**typename** identifier> function_declaration;
```

```
template <class myType>
myType GetMax <myType a, myType b> {
    return (a > b ? a:b)
}
// Call this function
k = GetMax<int>(i, j);
```
