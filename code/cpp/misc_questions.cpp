#include<stdio.h>
#include<string.h>



int round_to_next_largest_multiple_n(int num_to_round, int multiple)
{
    if (multiple == 0){
        return num_to_round;
    }

    int remainder = num_to_round % multiple;
    if (remainder == 0){
        return num_to_round;
    }
    return num_to_round + multiple - remainder;
}



int main(){
    int res = round_to_next_largest_multiple_n(55, 16);
    printf("Result of rounding %d \n", res);
    return 0;
}
