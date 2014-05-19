/*
 * Vorname: Christian
 * Nachname: Rebischke
 */

public class Car {
	/**
	 * @author Christian Rebischke
	 * @version 1.0
	 * A simple Car Application
	 * @param mileage - Kilometerstand
	 * @param PetrolTank - Die Tank-Klasse
	 * @param usedMotor - Motor-Klasse
	 */
  int mileage;
  PetrolTank usedTank;
  Motor usedMotor;

  public Car(int mileage, Motor usedMotor, PetrolTank usedTank)
  {
	  /**
	   * Car
	   * Konstruktor der Car-Klasse
	   * @param mileage - Kilometerstand
	   * @param PetrolTank - Die Tank-Klasse
	   * @param usedMotor - Motor-Klasse
	   */
    this.mileage = mileage;
    this.usedMotor = usedMotor;
    this.usedTank = usedTank;
  }
  public static void main(String[] args) {
	  /**
	   * Main Funktion
	   * Als Beispiel habe ich hier mal einen Porsche genommen :)
	   */
    Car porsche = new Car(10_000, new Motor(12.5), new PetrolTank(70,30));
    porsche.printCarInfo();
    porsche.driveInt(23);
    porsche.printCarInfo();

  }
  
  public void printCarInfo()
  {
	  /**
	   * printCarInfo
	   * Gibt Informationen über Tank und Kilometerstand aus
	   */
    System.out.println("km: "+mileage +"\tTank"+usedTank.getActualCapacity());
  }
  
  public void driveInt(int kilometers)
  {
	  /**
	   * driveInt
	   * Die Fahrfunktion 
	   */
    double consumption = usedMotor.getConsumptionPer100km()*((double)kilometers/100);
    usedTank.reduceActualCapacity((int)consumption);
  }

}
