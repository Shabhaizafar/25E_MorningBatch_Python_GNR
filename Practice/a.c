#include<stdio.h>

void main(){
    long int a, b, gcd, remainder;
    printf("Enter the value of a :");
    scanf("%ld",&a);
    printf("Enter the value of b :");
    scanf("%ld",&b);
    while(b != 0){
        remainder = a % b;
        a = b;
        b = remainder;
    }
    gcd = a;
    printf("GCD : %ld\n",gcd);
}