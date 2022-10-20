#include <stdio.h>
#include <stdlib.h>

double average(double a, double b)
{
    double avg = 0.5*a + 0.5*b;
    return avg;
}

int main()
{
    double a = 0;
    double b = 0;
    printf("Enter two numbers and I will find the average\n");
    scanf("%lf\n", &a);
    scanf("%lf\n", &b);
    double c = average(a,b);
    printf("%lf",c);
}
