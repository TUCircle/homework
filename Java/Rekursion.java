// Zinssatz Rekursiv von Christian Rebischke

import java.lang.Math.*;

class Rekursion
{
  private static final double kapital = 10000.0;
  private static final double zinsen = 0.02;
  private static double[] array = new double[7];
  private static final int laufzeit = 6;

  public static void main(String[] argv)
  {
  rekursion(kapital, laufzeit);
  output();
  }

  private static void output()
  {
    int k = 0;
    System.out.println("Kapitalentwicklung mit Rekursion");
    for(double i : array) System.out.println("Jahr "+(k++)+": "+i);
  }
  
  private static double rekursion(double startkapital,int i)
  {
    array[i] = startkapital * Math.pow((1 + zinsen), i);    
    if(i == 0) 
    { 
      return kapital;
    }
    else
    {
      rekursion(startkapital, --i);
      return startkapital;
    }
  }
}
