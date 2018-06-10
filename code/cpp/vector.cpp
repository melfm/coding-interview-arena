// Implement a Vector class data-structure in C++
// Work in progress ...

class vector {

    int sz;
    double* elem;

    void copy(const vector& arg); // copy elements from arg into elem

public:
    vector(const vector&); // copy constructor: define copy

};

void vector::copy(const vector& arg)
{
    for (int i=0; i<arg.sz; ++i) elem[i] = arg.elem[i];
}

vector::vector(const vector& arg)
    :sz(arg.sz), elem(new double[arg.sz])
{
    copy(arg)
}

vector& vector::operator=(const vector& a)
{
    double* p = new double[a.sz];   // allocate new space
    for(int i=0; i<a.sz; ++i) p[i]=a.elem[i];   // copy elements
    delete[] elem;  // deallocate old space, this is from target vector
    elem = p;       // now reset elem
    sz = a.sz;
    return *this;   // return a self-reference
}
