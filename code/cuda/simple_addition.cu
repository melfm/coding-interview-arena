#include <stdio.h>

__global__ void add(int *a, int *b, int *c){
    *c = *a + *b;
}


int main(void) {

    //////////////////////
    // Integer Addition
    /////////////////////
    int a, b, c;
    int *d_a, *d_b, *d_c;

    int size = sizeof(int);

    // Allocate space for device copies
    cudaMalloc((void **)&d_a, size);
    cudaMalloc((void **)&d_b, size);
    cudaMalloc((void **)&d_c, size);

    a = 10;
    b = 7;

    // Copy inputs to device
    cudaMemcpy(d_a, &a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, &b, size, cudaMemcpyHostToDevice);

    // Launch the kernel
    add<<<1,1>>>(d_a, d_b, d_c);

    // Copy results back
    cudaMemcpy(&c, d_c, size, cudaMemcpyDeviceToHost);

    printf("Int Addition :  %d + %d = %d \n",a , b, c);

    // Clean up
    cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);

    return 0;
}
