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
    for (count = 0 ; x!= 0; x>>=1)
    {
        if (x & 01)
            count++;
    }
    return count;
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

    int bit_count = Bitcount(24);
    // 24 -> 11000
    printf("Bit count = %d \n", bit_count);
    int res = swapBits(28, 0, 3, 2);
    // Expected result -> 7
    printf("Result = %d \n", res);
    return 0;
}

