

public class Motor {
	/**
	 * Die MotorKlasse
	 * @param consumptionPer100km; - verbrauch pro 100km
	 */
  private double consumptionPer100km;
  
  public Motor(double consumptionPer100km)
  {
		/**
		 * Konstruktor für die Motorklasse
		 * @param consumptionPer100km; - verbrauch pro 100km
		 */
    this.consumptionPer100km = consumptionPer100km;
  
  }
  
  public double getConsumptionPer100km()
  {
	  /**
	   * Get-Funktion für den Verbrauch
	   */
    return consumptionPer100km;
  }

}
