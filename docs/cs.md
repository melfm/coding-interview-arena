# Computer Science Concepts

## Stack vs Heap
### Stack
- Stored in computer RAM just like the heap
- Variables created on the stack will go out of scope and are automatically deallocated.
- Faster to allocate than on heap
- Implemented with an actual stack data structure

### Heap
- In c++ variables on the heap must be destroyed manually using `free` or `delete`.
- Used in demand to allocate a block of memory
- Responsible for memory leaks

## Compiled vs Interpreted Languages
- A compiled language code once compiled, is expressed in the instructions of the target machine.
- An interpreted langugage is one where the instructions are not directly executed by the target machine but instead read and executed by some other program.

### Python
- Source code is first compiled to byte code as *.pyc*. This byte code can be interpreted (CPython or JIT compiled PyPy).

### JIT compiler
- The compiler runs **after** the program has started and compiles the code on the fly into a form that's usually faster.
- A JIT has access to dynamic runtime information whereas a standard compiler doesn't and can make better optimizations like inlining functions that are used frequently.

## Dynamic Type Checking
- Process of verifying the type safety of a program at runtime.
- For instance Python features a dynamic type system.

## Dynamic Programming
- Method for solving complex problems by breaking it down into a collection of simpler subproblems, solving each of those sub-problems once and storing their solutions.
- The next time the sub-problem occurs instead of recomputing its solution, it can look up the previously computed solution.
- E.g. is Fibonacci sequence, Dijkstra's algorithm for the shortest path problem

```
function fib(n)
    if n <= 1 return n
        return fib(n − 1) + fib(n − 2)
```
- Note how the recursive function above, needs to re-calculate for the same *n*.
- Instead if we could use more space, we can re-write this as :

```
var m := map(0 → 0, 1 → 1)
function fib(n)
    if key n is not in map m
        m[n] := fib(n − 1) + fib(n − 2)
    return m[n]
```
- This technique of saving values that have already been calculated is called **memoization**.
