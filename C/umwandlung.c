#include <stdio.h>
#include <stdlib.h>
#define SIZE 32

int* calc(int source, int  base)
{
  int i;
  int *p = NULL;
  int *array = (int*) calloc(SIZE, SIZE*sizeof(int));
  p = &array[SIZE-1];
  do
  {
    *p = source % base;
    source = source / base;
    p--;
  }while(source != 0);

  p = &array[0];
  return p;
}


void output(int *array)
{
  int i;
  printf("Das Ergebnis lautet: ");
  for(i=0; i!= SIZE ; i++)
  {
    printf("%d%", array[i]);
  }
  printf("\n");
}

int main(void)
{
  const int source;
  const int base;
  int *p;

  printf("Herzlich Willkommen beim Umrechner\n");
  printf("Bitte Dezimalzahl eingeben: ");
  scanf("%d", &source);
  printf("Bitte Basis eingeben: ");
  scanf("%d", &base);
  
  p = calc(source, base);
  output(p);
  free(p);
  return 0;
}
