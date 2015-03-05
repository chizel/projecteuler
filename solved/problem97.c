#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define ARR_SIZE 15

void power2(void);
void print_number(unsigned char *);

int main(int argc, char *argv[])
{
    long long res;
    power2();
    return EXIT_SUCCESS;
}

void power2(void)
{
    unsigned char tmp, digits[ARR_SIZE];
    int i, j, k;
    unsigned long long res = 0;
    uint32_t degree;

    for(i = 0; i < ARR_SIZE; i++)
    {
        digits[i] = 0;
    }

    digits[ARR_SIZE - 1] = 1;

    tmp = 0;
    degree = 7830457;

    for(i = 1; i <= degree; i++)
    {
        for(j = ARR_SIZE - 1; j >= 0; j--)
        {
            digits[j] *= 2;
            digits[j] += tmp;
            tmp = digits[j] / 10;
            digits[j] = digits[j] % 10;
        }

        tmp = 0;
    }

    print_number(digits);

    for(i = 0; i < ARR_SIZE; i++)
    {
        printf("%d", digits[i]);
        res += digits[i];
        res *= 10;
    }
    putc('\n', stdout);

    res /= 10;
    res %= 10000000000;
    printf("result: %llu\n", res);
    res *= 28433;
    res += 1;
    res %= 10000000000;
    printf("result: %llu\n", res);
}

void print_number(unsigned char *p)
{
    unsigned char i;
    for(i = 0; i < ARR_SIZE; ++i)
    {
        putc('0' + p[i], stdout);
    }

    putc('\n', stdout);
}
