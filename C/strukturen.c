#include <stdio.h>
#include <stdlib.h>

typedef char *string;


struct customer{
    string firstname;
    string lastname;
    string street;
    int housenumber;
    enum{
      private,
      commercial,
      } customertype;
    union{
      int accountantnumber;
      string id;
      } credentials;
    };

int main(void){
  const char *types[] = {
    [private] = "private",
    [commercial] = "commercial",
    };
  struct customer* newcustomer = malloc(sizeof(struct customer));
  if(newcustomer){
    //OPTIONAL struct customer* newcustomer = (struct customer*) malloc(sizeof(struct customer));
    newcustomer->firstname = "Fantasiename";
    newcustomer->lastname = "foobarfoo";
    newcustomer->street = "fantasiestraße";
    newcustomer->housenumber = 1337;
    newcustomer->customertype = private;
    newcustomer->credentials.accountantnumber = 1354645654;
    printf("Vorname: %s\n", newcustomer->firstname);
    printf("Nachname: %s\n", newcustomer->lastname);
    printf("Straße: %s\n", newcustomer->street);
    printf("hausnummer: %d\n", newcustomer->housenumber);
    printf("ID: %d\n", newcustomer->credentials.accountantnumber);
    printf("Kundentyp: %s\n", types[newcustomer->customertype]);
    free(newcustomer);
    return 0;
    }
  else{
    printf("Fehler bei der Speicherreservierung\n");
    return 1;
    }
  }



