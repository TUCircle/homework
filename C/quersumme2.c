#include <stdio.h>
#include <stdlib.h>


int quersumme(int x)
{
  int sum = 0;
  while( x > 0)
  {
    sum += x % 10;
    x /= 10;
    
  }
  return sum;
}



int main(int argc, char *argv[])
{
  int number;
  if(argc != 2)
  {
    printf("Zu wenig oder zu viele Argumente\n");
    return 1;
  }
  number = atoi(argv[1]);
  while(1)
  {
    if(number > 0)
    {
      printf("Die Zahl ist %d\n", number);
      printf("Ergebnis: %d\n", quersumme(number));
      return 0;
    }

    if(number < 0)
    {
      printf("Zahl kleiner 0 neue Zahl: ");
      scanf("%d", &number);
    }
  }
    

}
