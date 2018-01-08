#include <stdio.h>


/* Bitwise operators in C
 * & -> Binary AND, copies bits to the result if
 *  it exists in both (001 & 011 -> 001)
 * | -> Binary OR, copies a bit if it exists in
 * either operand (001 | 011 -> 011)
 * ^ -> Binary XOR copies bits if it is set in
 *  one operand but not both (001 ^ 011 -> 010)
 *  ~ -> Binary Ones Complement op is unary and
 *   has the effect of `flipping` bits (~001 -> 110)
 * << -> Binary Left Shift Op. The left operands value
 *  is moved left by the number of bits specified by
 *  right operand (001 << 2 -> 100)
 * >> -> Binary Right Shift Op. The left operands value
 *  is moved right by the number of bits specified by
 *  the right operand (001 >> 2 -> 000)
 */


// Write a function, Bitcount, that counts bits set to 1
int Bitcount(unsigned char x)
{
    int count;
    int i = 0;
    // char size is 8 bits
    for (i = 0 ; i < 8; i++)
    {
        if (x & 0b00000001)
            count++;
        x = x >> 1;
    }

    return count;
}


// Given a binary number, reverse the bits
unsigned int reverseBits(unsigned int x)
{
    unsigned int num_of_bits = sizeof(x) * 8;
    unsigned int reversed_x = 0;
    int i = 0;
    unsigned int tmp;

    for(i = 0; i < num_of_bits; ++i)
    {
        tmp = (x & (1 << i));
        if (tmp)
            reversed_x |= (1 << (num_of_bits - 1) - i);
    }
    return reversed_x;
}

void print_binary(unsigned n)
{
    unsigned i;
    for (i = 1 << 31; i > 0; i = i / 2)
        (n & i)? printf("1"): printf("0");
}

// Given a number x and two positions from right,
// in binary write a function that swaps n bits
// at given two positions
int swapBits(unsigned int x, unsigned int p1,
             unsigned int p2, unsigned int n)
{
    // Move all bits from first set to rightmost side
    // 1U is an unsigned value 1
    // So 1U << 0 is shifted to the left by 0 bits
    unsigned int set1 = (x >> p1) & ((1U << n) - 1);

    // Move all bits of second set to rightmost side
    unsigned int set2 = (x >> p2) & ((1U << n) -1);

    // XOR the two sets
    unsigned int xor = (set1 ^ set2);

    // Put the xor bits back to their original pos
    xor = (xor << p1) | (xor << p2);

    // Put the xor with the original number to swap the sets
    unsigned int result = x ^ xor;

    return result;
}

int main()
{

    ////////////////
    // BitCount
    ////////////////
    int bit_count = Bitcount(24);
    // 24 -> 11000
    printf("Bit count of 24 = %d \n", bit_count);

    ////////////////
    // BitReverse
    ////////////////
    unsigned int x = 24;
    print_binary(x);
    printf("\n");

    unsigned int reversed_x = reverseBits(x);
    printf("Reversed bits ->\n");
    print_binary(reversed_x);
    printf("\n");

    ////////////////
    // BitSwap
    ////////////////

    int res = swapBits(28, 0, 3, 2);
    // Expected result -> 7
    printf("Result = %d \n", res);

    return 0;
}

