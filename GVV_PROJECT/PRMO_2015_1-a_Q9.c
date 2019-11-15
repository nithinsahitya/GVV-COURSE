#include<stdio.h>

int l1,b1,l2,b2, r1[2],r2[2],i,d;
int main()
{
    l1=printf("Enter l1 : ");
    scanf("%d",&l1);
    b1=printf("Enter b1 : ");
    scanf("%d",&b1);
    l2=printf("Enter l2 : ");
    scanf("%d",&l2);
    b2=printf("Enter b2 : ");
    scanf("%d",&b2);
    if (l1>b1)
    {r1[1]=l1;r1[0]=b1;
    }
    else
    {
        r1[1]=b1;r1[0]=l1;
    }
    if (l2>b2)
    {r2[1]=l2;r2[0]=b2;
    }
    else
    {
        r2[1]=b2;r2[0]=l2;
    }


    if (r1[1]>r2[1])
    {
        i=r1[1];
        d=r1[1]-r1[0];
    if (r2[0]<=d)
       {

        printf("The side of side is %d \n",i);
        printf("The minimum area of  the square is %d sq.units",i*i);
        }
    else
        {
           i+=r2[0]-d;
           printf("The minimum side is %d \n",i);
           printf("The minimum area of  the square is %d sq.units",i*i);
        }
    }
    else
    {
        i=r2[1];
        d=r2[1]-r2[0];
        if (r1[0]<=d)
        {
            printf(" The minimum side is %d\n",i);
            printf("The minimum area of  the square is %d sq.units",i*i);
        }
        else{
            i+=r1[0]-d;
            printf("The minimum side is %d \n",i);
            printf("The minimum area of the square is %d sq.units",i*i);
        }
    }
}
