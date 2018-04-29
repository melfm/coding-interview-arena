# Python Concepts

## Iterables
- When you create a list, you can read its items one by one, it's called iteration.
- A list comprehension is also a list and so an interable.
```
mylist = [x*x for x in range(3)]
```
- You can read the iterables as much as you want, they are stored in memory.

## Generators
- Generators are iterators, but you can only iterate over them once.
- They do not store all the values in memory, they generate the values on the fly.
```
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)
```
- You cannot perform `for i in my generator` a second time since generators can only be used once. They calculate `0` and forget about it, then calculate `1` and so on.

## Yield
- A keyword used like `return`, except that the function will return a generator.
```
def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i
>>> mygenerator = create_generator()
>>> for i in mygenerator:
        print(i)
```
- When you call the function, the code inside the function body does not run.
- The function only returns the generator object. The code will be run each time the `for` uses the generator.
- The first time the `for` calls the generator object created from the function, it will run the code in the function from the beginning until it hits `yield`, then it'll return the first value of the loop.
- Then each other call will run the loop and return the next value, until there is no value to return.

### Summary of Python's Generators vs Iterators
- Every generator is an iterator, but not vice versa.
- A generator is a subset of an interator.
- A Generator is called by calling a function that has a *yield* expression.
- Iterators are objects that have an *__iter__* and *__next__* method.




