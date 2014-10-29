
public class BankAccount {
	/**
	 * BankAccount
	 * @param accountIdentificationNumber - Kontonummer
	 * @param creditBalance - Kontostand
	 */
	private int accountIdentificationNumber;
	private int creditBalance;

	public BankAccount(int accountIdentificationNumber,int creditBalance)
	{
		/**
		 * BankAccount
		 * Konstruktor für die Klasse BankAccount
		 */
		this.accountIdentificationNumber = accountIdentificationNumber;
		this.creditBalance = creditBalance;
	}
	
	public int getAccountIdentificationNumber()
	{
		/**
		 * getAccountIdentificationNumber
		 * getter Funktion für die AccountIdentificationNumber
		 */
		return accountIdentificationNumber;
	}
	
	public int getCreditBalance()
	{
		/**
		 * getCreditBalance
		 * getter Funktion für die creditbalance
		 */
		return creditBalance;
	}
	
	public void setAccountIdentificationNumber(int accountIdentificationNumberInput)
	{
		/**
		 * setAccountIdentificationNumber
		 * setter Funktion für die AccountIdentificationNumber
		 */
		this.accountIdentificationNumber = accountIdentificationNumberInput;
	}
	
	public void setCreditBalance(int creditBalanceInput)
	{
		/**
		 * setCreditBalance
		 * setter Funktion für die creditbalance
		 */
		this.creditBalance = creditBalanceInput;
	}
}

