// Zinsenberechnung von Christian Rebischke

import java.lang.Math.*;

class Zinsen{

  public static void main( String[] args){
    int Startkapital = 10000; 
    int Laufzeit = 6;
    double Zinsen = 0.02; 

    System.out.println("Initiiere Schleife mit Laufzeit: " + Laufzeit + " und Startkapital: " + Startkapital);
    
    for(int i=1; i<(Laufzeit+1); i++){
      System.out.println("Konstanter Zinssatz für das Jahr: " + i + " ist: " + Startkapital*(i*Zinsen+1));
      System.out.println("Exponentieller Zinseszinssatz für das Jahr: " + i + " ist: " + Startkapital * Math.pow((1+Zinsen), i));
    }  
  }
}
