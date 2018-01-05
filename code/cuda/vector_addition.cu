#include <stdio.h>


__global__ void add(int *a, int *b, int *c) {
	c[blockIdx.x] = a[blockIdx.x] + b[blockIdx.x];
}

void random_ints(int* a, int N){
    int i;
    for (i = 0; i < N; ++i){
        // Rand number between 0 - 19
        a[i] = rand() % 20;
    }
}

#define N 20

int main(void) {

    //////////////////////
    // Vector Addition
    /////////////////////

    // host copies of a, b, c
	int *a, *b, *c;
    // device copies of a, b, c
	int *d_a, *d_b, *d_c;
	int size = N * sizeof(int);

	// Alloc space for device copies of a, b, c
	cudaMalloc((void **)&d_a, size);
	cudaMalloc((void **)&d_b, size);
	cudaMalloc((void **)&d_c, size);

	// Alloc space for host copies of a, b, c
	// Setup input values
	a = (int *)malloc(size); random_ints(a, N);
	b = (int *)malloc(size); random_ints(b, N);
	c = (int *)malloc(size);

    for(int i=0; i< N; i++)
    {
        printf("Input vector a + b: %d + %d = %d\n",
                a[i], b[i], a[i] + b[i]);
    }

	// Copy inputs to device
	cudaMemcpy(d_a, a, size, cudaMemcpyHostToDevice);
	cudaMemcpy(d_b, b, size, cudaMemcpyHostToDevice);

	// Launch add() kernel on GPU with N blocks
	add<<<N,1>>>(d_a, d_b, d_c);

	// Copy result back to host
	cudaMemcpy(c, d_c, size, cudaMemcpyDeviceToHost);

    for(int i=0; i< N; i++)
    {
        printf("Vector Addition Result : %d \n", c[i]);
    }

	// Cleanup
	free(a); free(b); free(c);
	cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);
	return 0;
}
