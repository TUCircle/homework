import javax.swing.JOptionPane;

/*
 * Vorname: Christian
 * Nachname: Rebischke
 */


public class Bank {
	/**
	 * @author Christian Rebischke
	 * @version 1.1
	 * A simple Bank Application
	 * @param bankIdentificationNumber - die Bankleitzahl
	 * @param ACCOUNT_MAXIMUM - zahl maximaler Konten
	 * @param USER_INFORMATION - Zahl maximaler Userinformationen -1 zb die Kontonummer
	 * @param accountDatabase - Die Accountdatenbank
	 * @Param BankAccount - Die Klasse für Konten
	 */
	int bankIdentificationNumber;
	final static int ACCOUNT_MAXIMUM = 3;
	final static int USER_INFORMATION = 2;
	static int[][] accountDatabase = new int[ACCOUNT_MAXIMUM][USER_INFORMATION];
	static BankAccount account;
	
	public Bank(int bankIdentificationNumber, BankAccount account)
	{
		/**
		 * Der Konstruktor für die Bank Klasse
		 */
		this.bankIdentificationNumber = bankIdentificationNumber;
		this.account =  account;
	}
	public static void main(String[] args) {
		/**
		 * Main funktion
		 * Hier laufen die ganzen Prozesse ab etc..
		 */
		Bank myBank = new Bank(853945748, new BankAccount(0,0));
		for(int i=0; i< ACCOUNT_MAXIMUM; i++)
		{
			account.setAccountIdentificationNumber(Integer.parseInt(JOptionPane.showInputDialog("Die Kontonummer:")));
			account.setCreditBalance(Integer.parseInt(JOptionPane.showInputDialog("Aktueller Kontostand:")));
			createNewBankAccount(account.getAccountIdentificationNumber(), account.getCreditBalance());
		}
		showAccountDatabase(myBank.bankIdentificationNumber);
		int transferValue = Integer.parseInt(JOptionPane.showInputDialog("Der zu überweisende Betrag: "));
		int sourceIdentificationNumber = Integer.parseInt(JOptionPane.showInputDialog("Quelle: "));
		int targetIdentificationNumber = Integer.parseInt(JOptionPane.showInputDialog("Ziel: "));
		moneyTransfer(transferValue, sourceIdentificationNumber, targetIdentificationNumber);
		showAccountDatabase(myBank.bankIdentificationNumber);

	}
	
	private static void moneyTransfer(int transferValue, int sourceIdentificationNumber, int targetIdentificationNumber)
	{
		/**
		 * moneyTransfer
		 * @param transferValue - Zu überweisender Betrag
		 * @param sourceIdentificationNumber - Quelle
		 * @param targetIdentificationNumber - Ziel
		 */
		int check = 0; //Check Variable ob beide Konten existieren
		for(int i = 0 ; i< accountDatabase.length ; i++)
		{
			if ( accountDatabase[i][0] == sourceIdentificationNumber) check++;
			if ( accountDatabase[i][0] == targetIdentificationNumber) check++;
		}
		if(check == 2) //Falls beide Konten existieren...
		{
			for(int i = 0 ; i< accountDatabase.length ; i++)
			{
				if ( accountDatabase[i][0] == sourceIdentificationNumber)
				{
					if((accountDatabase[i][1] - transferValue) < 0) System.out.println("Nicht genug Geld auf dem Konto!");
					else accountDatabase[i][1] = accountDatabase[i][1] - transferValue;
				}
			}
			for(int i = 0 ; i< accountDatabase.length ; i++)
			{
				    if ( accountDatabase[i][0] == targetIdentificationNumber)
					{
						accountDatabase[i][1] = accountDatabase[i][1] + transferValue;
					}
				    
			}
			
		}
		else System.out.println("Eines oder beide Konten existieren nicht!");	
	}
	private static  void createNewBankAccount(int accountIdentificationNumber, int creditBalance)
	{
		/**
		 * createNewBankAccount
		 * Zum erstellen von Bankaccounts
		 * @param accountIdentificationNumber - Kontonummer
		 * @param creditBalance - Kontostand
		 */
		for(int i = 0 ; i< accountDatabase.length ; i++)
		{
			if ( accountDatabase[i][0] == 0)
			{
				accountDatabase[i][0] = accountIdentificationNumber;
				accountDatabase[i][1] = creditBalance;
				return;
				
			}
		}
		
	}
	private static void showAccountDatabase(int bankIdentificationNumber)
	{
		/**
		 * showAccountDatabase
		 * @param bankIdentificationNumber - Bankleitzahl
		 *  Letzter Bugfix: Falls Betrag kleiner 10 wird 0,0x ausgegeben statt 0,3 
		 */
		System.out.println("Bankleitzahl: "+ bankIdentificationNumber);
		for(int i=0; i < accountDatabase.length ; i++)
		{
			System.out.println("---------------------");
			System.out.println("Kontonummer: "+ accountDatabase[i][0]);
			System.out.print("Kontostand: "+ (accountDatabase [i][1]/ 100 ) + ",");
			if((accountDatabase[i][1] % 100) < 10)
				System.out.print("0");
			System.out.println((accountDatabase[i][1] % 100) + "€");
			System.out.println("---------------------");
		}
	}

}
