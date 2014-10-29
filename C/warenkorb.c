 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 //Konstante für Rückgabewert
 #define SUCCESS 0

 /*Aufgabe 1a struct mit typedef um später einfacher auf 
 struct zugreifen zu können und für weniger Schreibarbeit*/


 typedef struct _Posten_
 {
   char* name_;
   int price_;
   struct _Posten_ *next_;
 } posten;

 /*Aufgabe 1b Initialisieren der Funktionen add_Posten, 
 remove_Posten, free_posten, output, und rekursiv
 Die vorgegebenen Funktionssignaturen wurden etwas verändert
 um lokal statt global auf die Variablen zuzugreifen.
 Globale Variablen sind zu fehleranfällig und sprechen
 gegen das Prinzip der modularen Programmierung
 wie es hier mit den Funktionen ja der Fall ist.
 */

 //addPosten-Funktion:
 int add_posten(char *name, int preis, posten *entry);

 //removePosten-Funktion:
 int remove_posten(int index, posten **entry);

 //Funktion zur Speicherverwaltung
 int free_posten(posten *to_free);

 //Funktionen zur Ausgabe
 void output(posten *out);
 void rekursiv(posten *out, int sum_rec);

 //================Funktionen: Anfang==========================
 int add_posten(char *name, int preis, posten *entry)
 {
   while (entry->next_ != NULL)
   {
     entry = entry->next_;
   }

   if (entry->name_ != NULL)
   {
     posten *new = (posten*) malloc(sizeof(posten));
     entry->next_ = new;
     entry = entry->next_;
   }
   /*strlen(name)+1 deshalb weil strlen nur den String 
    ohne den Terminierungsoperator \0 zählt deshalb +1
    das strcpy ist notwendig weil sonst immer auf die 
    gleiche Speicheradresse geschrieben werden würde
    und so alle Produkte den gleichen Namen hätten
   */
   entry->name_ = (char*) malloc(strlen(name) + 1);
   strcpy(entry->name_,name);
   entry->price_ = preis;

   return SUCCESS;
 }

 //remove_posten funktion
 int remove_posten(int index, posten **entry)
 {
   int i = 0;
   posten *work = *entry;

   for(i = 0; i < (index - 1); ++i)
   {
     work = work->next_;
   }

   posten *to_del = NULL;

   if(index == 0)
   {
     *entry = work->next_;
     to_del = work;
   }
  else
  {
    to_del = work->next_;
    work->next_ = to_del->next_;
  }

  free(to_del->name_);
  free(to_del);
  to_del = NULL;

  return SUCCESS;
}

 //Kleine Bonusfunktion zum Säubern des Speichers
 //Ist allerdings noch nicht ausgereift
 //So liefert das Memory-Detection-Tool "valgrind" 
 //noch mehrere Errors
 //im Memory-Management
 int free_posten(posten *to_free){
   posten *tmp;
   tmp = to_free->next_;
   if(tmp == NULL) return SUCCESS; 
   free(to_free->name_);
   free(to_free);
   free_posten(tmp);
 }
 
  

 //Aufgabe 1c: Schleifen-Output
 void output(posten *out)
 {
   //Zähler für Kunden-Freundlichkeit :)
   int counter = 0;
   int sum = 0;
   int cents = 0;
   printf("------------------------------------------------\n");
   while(out)
   {
     printf("%d. Produktname: %s ", counter, out->name_);
     printf("Produktpreis %d\n", out->price_);
     sum += out->price_;
     out = out->next_;
     counter++;
   }
 cents = sum % 100;
 sum /= 100;
 printf("------------------------------------------------\n");
 printf("Summe der Produkte: %d,%d€\n", sum, cents);
 printf("------------------------------------------------\n");
 }

 //Aufgabe 1c: Rekursiver Output
 void rekursiv(posten *out, int sum_rec)
 {
  printf("Produktname: %s ", out->name_);
  printf("Produktpreis %d\n", out->price_);
  sum_rec += out->price_;
  out = out->next_;
  if(out==NULL)
  {
    int cents = 0;
    cents = sum_rec % 100;
    sum_rec /= 100;
    printf("------------------------------------------------\n");
    printf("Summe der Produkte: %d,%d\n", sum_rec, cents);
    printf("------------------------------------------------\n");
    return;
  }
  rekursiv(out, sum_rec); //rekursiver Aufruf
 }

 //================Funktionen: Ende==========================

int main(void)
{
  int sum_rec = 0;
  int opt, price, index;
  char *name = (char*) malloc(20);
  //Initialisieren eines Startpunkts
  posten *start = (posten*) malloc(sizeof(posten));

  while(1)
  {
    //Kundeninterface
    printf("------------------------------------------------\n");
    printf("Was möchten Sie tun?\n");
    printf("------------------------------------------------\n");
    printf("1) Produkt dem Warenkorb hinzufügen\n");
    printf("2) Produkt aus Warenkorb entfernen\n");
    printf("3) Warenkorb ausgeben (normal)\n");
    printf("4) Warenkorb ausgeben (rekursiv)\n");
    printf("0) Programm beenden\n");
    printf("Ihre Eingabe: ");
    scanf("%d", &opt);

    switch(opt)
    {
      case 1:
        printf("Name: ");
        scanf("%s", name);
        printf("Preis: ");
        scanf("%d", &price);
        add_posten(name, price, start);
        break;
      case 2:
        output(start);
        printf("------------------------------------------------\n");
        printf("Achtung es wird beim Zählen mit 0 angefangen!!! \n");
        printf("------------------------------------------------\n");
        printf("Zu löschendes Produkt: ");
        scanf("%d", &index);
        remove_posten(index, &start);
        break;
      case 3:
        output(start);
        break;
      case 4:
        printf("------------------------------------------------\n");
        rekursiv(start, sum_rec);
        printf("------------------------------------------------\n");
        break;
      case 0:
        free_posten(start);
        return SUCCESS;
      default:
        printf("Fehlerhafte Eingabe!");
        break;
    }
  }
}


