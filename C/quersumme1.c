#include <stdio.h>

/*  Programm zur Berechnung von Quersummen */

/*  typedef für unsigned int
    Wir hätten auch size_t nehmen können
    aber uint klingt logischer */

typedef unsigned int uint;


/*  Funktion Quersumme die ein Array als Parameter lädt
    und ein Ergebnis als integer zurück gibt */

int quersumme(char *digits){
  //lokale Variablen initialisieren
  uint ergebnis = 0;
  uint i;
  
  /* !(digits[i]=='\0') deshalb weil strings in C
     immer ein Terminierungssymbol '\0' am Ende 
     haben.Das - '0' ist dafür da um von ASCII zu 
     Integer zurück zu rechnen. '0' == 48, '1' == 49
     usw....   */
  
  for(i=0; !(digits[i]=='\0'); i++){
    printf("%d = %d\n", i, (uint)(digits[i] - '0'));
    ergebnis +=(uint)(digits[i] - '0');
    }
  return ergebnis;
  }



int main(void){
  //Initialisieren der lokalen Variablen und des Arrays mit '0'
  uint i;
  int input = 0;
  char array[64];
  for(i=0; i < 64; i++){
    array[i] = '0';
    }

  //Kommandointerface
  printf("Herzlich willkommen beim Quersummen-Rechner\n");
  printf("Eingabe von Null beendet das Programm\n");
  while(1){
    printf("--------------------------------------------\n");
    printf("Eine Null eingeben zum beenden oder \n");
    printf("eine ganze Zahl eingeben zum Berechnen\n");
    printf("der Quersumme: ");
    
    /* If-Block zur Überprüfung ob ASCII zeichen
       eingegeben worden sind. Falls ja
       wird der STDIN (Standard Input) 
       zurückgesetzt. Dabei wird überprüft ob bei
       scanf etwas eingegeben worden ist oder nicht.
    */
  
    if( scanf("%d", &input) <= 0){
      printf( "\nFehler bei der Eingabe\n");
      while ( getchar() != '\n' );
      continue;
      }
    
    if( input > 0 ){
      sprintf(array, "%d", input);
      printf("Quersumme: %d\n", quersumme(array));
      }

    else if( input == 0){
      printf("Es wurde 0 eingegeben. Ergebnis ist 0.\n");
      printf("Program wird beendet!\n");
      break;
      }
    else{
      printf("Fehler bei der Eingabe!\n");
      printf("Keine negativen Zahlen!\n");
      }

   }
//Programm Ende
return 0;
}
