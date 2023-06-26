#include <stdio.h>
int slargest(int a,int b,int c){
    if((a>=b && a>=c) || (a<=b && a>=c))
        return a;
    else if((b>=a && b<=c) || (b<=a && b>=c))
        return b;
    else
        return c;
}
int main()
{
    int m,n,k;
    printf("enter m");
    scanf("%d",&m);

    printf("enter n");
    scanf("%d",&n);

    printf("enter k");
    scanf("%d",&k);

    int result =slargest(m,n,k);
    printf("%d",result);
}