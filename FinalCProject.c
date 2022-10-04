#include <stdio.h>
#include <stdlib.h>
#include<math.h>
char shape_letter ;
double shape_length;
int main()
{
   printf("Enter The First Letter Of The Shape Name : ");
   scanf("%c", &shape_letter);
   function1();
   return 0;
}
void function1(){
      if(shape_letter == 's' )
       {
         square();
       }
       else if (shape_letter == 'p')
       {
           pyramid();
       }
       else if (shape_letter == 't')
       {
           triangle();
       }
       else if (shape_letter == 'c'){
           circle();
       }
       else
       {
          printf("Invalid Letter. ");
       }
 return;
}
void function2(){
   do{
    printf("Enter the length:");
    scanf("%lf", &shape_length);
   }while( shape_length<0);
   function1();
 return;
}
void function3()
{
   char decision;
   printf("Enter Y to draw anthor shape Or  N to End porgram ");
   scanf("%c" , decision);
   if(decision == 'Y')
   {
     function2();
   }
   else if (decision == 'N')
   {
      printf("Program Ended ");
   }
   else
   {
      printf("Invalid Choice\n");
      function3();
   }
 return;
}
void pyramid(){
    do{
    printf("Enter the length:");
    scanf("%lf", &shape_length);
   }while( shape_length<0);
    int totalrows,row,space,star;
    for(row=1 ; row<=shape_length ; row++)
    {
        for( space=1; space<=(shape_length-row) ; space++)
        printf(" ");
        for( star=1; star<=((2*row)-1); star++)
        printf("*");
        printf("\n");
    }
   return;
}
void square(){
    do{
    printf("Enter the length:");
    scanf("%lf", &shape_length);
   }while( shape_length<0);
    int i, j, n;
    for(i=1; i<=shape_length; i++){
        for(j=1; j<=shape_length; j++){
            if( i==1 || i==shape_length || j==1 || j==shape_length){
                printf("* ");
            }else{
                printf("  ");
            }
        }
        printf("\n");
    }
  return;
}
void triangle(){
    do{
    printf("Enter the length:");
    scanf("%lf", &shape_length);
   }while( shape_length<0);
    int numberofrows = 0;
    for(int rownum = 1; rownum<= shape_length;rownum++){
        for(int column = 1; column<= rownum;column++){
            printf("* ");
        }
        printf("\n");
    }
 return;
}
void circle(){
    do{
    printf("Enter the Radius:");
    scanf("%lf", &shape_length);
   }while( shape_length<0);

    int circle_rows, circle_columns;

    for (circle_rows=0; circle_rows<(2 * shape_length +1);circle_rows++){
        for(circle_columns=0; circle_columns<(2 * shape_length +1);circle_columns++){

            if(pow(circle_rows - shape_length,2) + pow(circle_columns - shape_length,2) <= pow(shape_length,2)+1){
                printf("*");    
            }
            else{
                printf(" ");
            }
            printf(" ");
        }
        printf("\n");
    }

 return; 
}