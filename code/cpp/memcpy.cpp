#include<stdio.h>
#include<string.h>

void myMemCpy(void *dest, void *src, size_t n)
{
    // The idea is to typecast given addresses to char
    // because char takes 1 byte
    // Typecast src and dest adresses to (char *)
    char *csrc = (char *)src;
    char *cdest = (char *)dest;

    // Copy contents of src[] to dest[]
    for (int i=0; i<n; i++)
        cdest[i] = csrc[i];
}

int main()
{
    // String copy
    char csrc[] = "CopyThisSentence";
    char cdest[100];
    myMemCpy(cdest, csrc, strlen(csrc)+1);
    printf("Copied string is %s", cdest);

    // Array copy
    int isrc[] = {10, 20, 30, 40, 50};
    int n = sizeof(isrc)/sizeof(isrc[0]);
    int idest[n], i;
    myMemCpy(idest, isrc, sizeof(isrc));
    printf("\nCopied array is ");
    for (i =0 ;i<n; i++)
        printf("%d ", idest[i]);
    printf("\n");
    return 0;
}
