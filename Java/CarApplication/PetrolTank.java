public class PetrolTank {
	/**
	 * PetrolTank
	 * Die Tank-Klasse
	 * @param capacity - Tankkapazität
	 * @param actualCapacity - aktuelle Füllung
	 */
  private double capacity;
  private double actualCapacity;
  
  public PetrolTank(double capacity, double actualCapacity)
  {
	  /**
	   * Konstruktor für die PetrolTank-Klasse
	   * @param capacity - Tankkapazität
	   * @param actualCapacity - aktuelle Füllung
	   */
    this.capacity = capacity;
    this.actualCapacity = actualCapacity;
  }
  
  public void reduceActualCapacity(double reduceFactor)
  {
	  /**
	   * reduceActualCapacity
	   * Reduziert/verbraucht die aktuelle Tankfüllung
	   * @param reduceFactor - Der Faktor um was reduziert werden soll
	   */
    this.actualCapacity-= reduceFactor;
    if(this.actualCapacity < 0.0) this.actualCapacity = 0.0;
         
  }
  
  public double getCapacity()
  {
	  /**
	   * getCapacity
	   * Getter für die Capacity
	   */
    return capacity;
  }
  
  public double getActualCapacity()
  {
	  /**
	   * getActualCapacity
	   * getter für die aktuelle Füllung
	   */
    return actualCapacity;
  }

}
