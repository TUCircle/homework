import javax.swing.JOptionPane;

/*
 * Vorname: Christian
 * Nachname: Rebischke
 */
public class BattleShip {
	/**
	 * @author Christian Rebischke
	 * @version 1.0
	 * A simple BattleShip game
	 * 
	 */
		

	public static void main(String[] args) {
		/**
		 * main 
		 * Hauptfunktion und Herz des BattleShip Games.
		 * Hier werden die eigentlichen Eingaben gemacht und der
		 * Programmfluss gesteuert
		 * 
		 */
		//Variablen sauber initialisieren..
		int[][] map = new int[10][10];
		int numberOfShips = 7;
		int xCord = 0;
		int yCord = 0;
		String insertType = "";
		//Karte mit 0 nullen initialisieren
		//Hab gehört die for-schleife ist unnötig da Java ein int-array schon mit 0 initialisiert
		//Aber ich machs mal trotzdem 
		map = createMap(map);
		for(int i=0; i < numberOfShips; i++){
			JOptionPane.showMessageDialog( null, "Dies ist die "+(i+1)+". Eingabe.\nAbbruch möglich mit exit");
			insertType = JOptionPane.showInputDialog("W für waagerecht - S für senkrecht");
			//exitfunction falls man früher raus will einfach exit eingeben
			//try-catch um ein Klicken auf "abbrechen" aufzufangen
			try {
			if(insertType.equals("exit")) break;
			}
			catch (java.lang.NullPointerException e){
				JOptionPane.showMessageDialog(null, "Es wurde Abbrechen angeklickt.\nZum Beenden exit eingeben");
				i--;
				continue;
			}
			//try-catch block zum catchen von fehlerhaften Input
			try {
				xCord = Integer.parseInt(JOptionPane.showInputDialog("Bitte X-Koordinate eintragen"));
				//Der Präinkrementor ist dazu da um die Eingabe so anzupassen das sie menschenfreundlicher ist
				//Also man gibt Zahlen zwischen 1 und 10 ein und nicht 0 bis 9 wie ja eigentlich ein 10-er Array
				//in Java aufgebaut ist. Gibt man also als X-Koordinate zb 2 ein ist damit die Zeile 1 gemeint.
				//Dies ist für den Endkunden "vertrauter" da die übliche Zählweise mit 1 beginnt nicht mit 0
				//wie in der Informatik.
				--xCord;
			} 
			catch (java.lang.NumberFormatException e) {
				JOptionPane.showMessageDialog(null, "Bitte Zahlen eingeben!");
				i--;
				continue;
			}	
			try {
				yCord = Integer.parseInt(JOptionPane.showInputDialog("Bitte Y-Koordinate eintragen"));
				//Der Präinkrementor ist dazu da um die Eingabe so anzupassen das sie menschenfreundlicher ist
				//Also man gibt Zahlen zwischen 1 und 10 ein und nicht 0 bis 9 wie ja eigentlich ein 10-er Array
				//in Java aufgebaut ist. Gibt man also als X-Koordinate zb 2 ein ist damit die Zeile 1 gemeint.
				//Dies ist für den Endkunden "vertrauter" da die übliche Zählweise mit 1 beginnt nicht mit 0
				//wie in der Informatik.
				--yCord;
			}
			catch (java.lang.NumberFormatException e) {
				JOptionPane.showMessageDialog(null, "Bitte Zahlen eingeben!");
				i--;
				continue;
			}
			//Funktionsaufruf durch meinen errorCodeParser: siehe Funktionsbeschreibungen
			if(errorCodeParser(checkInput(insertType, xCord, yCord, map)))
				map = placeShip(insertType , xCord, yCord, map);
			else i--;
		}
		outputMap(map);
	}

	
	public static int[][] createMap(int[][] map){
		/**
		 * createMap
		 * Diese Funktion erstellt die Spielkarte
		 * 
		 * @param map Die Spielkarte
		 * @return Die Spielkarte initialisiert mit Nullen
		 */
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[i].length; j++) {
				map[i][j] = 0;
			}
		}
		return map;
	}

	public static int checkInput(String insertType, int xCord, int yCord, int[][] map){
		/**
		 * checkInput
		 * Diese Funktion überprüft die Eingabe auf Fehler
		 * 
		 * @param insertType Der Platzierungsmodus für das Schiff W oder S
		 * @param xCord Die X-Koordinate
		 * @param yCord Die Y-Koordinate
		 * @param map Die Spielkarte nur zum überprüfen
		 * @return verschiedene Errorcodes 
		 * 
		 * Errorcode-Beschreibung:
		 * Error 1: Falscher Platzierungsmodus. Muss W oder S sein.
		 * Error 2: Falsche X-Koordinate bei Platzierungsmodus W.
		 * Error 3: Falsche Y-Koordinate bei Platzierungsmodus W.
		 * Error 4: Falsche X-Koordinate bei Platzierungsmodus S.
		 * Error 5: Falsche Y-Koordinate bei Platzierungsmodus S.
		 * Error 6: Platz für Schiff bereits vergeben.
		 * Error 0: Alles ok.
		 *
		 */
		if(!(insertType.equals("W") || (insertType.equals("S")))) return 1; 
		if(insertType.equals("W") && !((xCord > 0) && (xCord < 9))) return 2; 
		if(insertType.equals("W") && !((yCord >= 0) && (yCord <= 9))) return 3; 
		if(insertType.equals("S") && !((xCord >= 0) && (xCord <= 9))) return 4; 
		if(insertType.equals("S") && !((yCord > 0) && (yCord < 9))) return 5; 
		//Überprüfung auf belegte Plätze
		if(insertType.equals("W")){
			if(!(((map[yCord][xCord] == 0) && (map[yCord][xCord-1] == 0)) && (map[yCord][xCord+1] == 0)))
				return 6;
		}
		if(insertType.equals("S")){
			if(!(((map[yCord][xCord] == 0) && (map[yCord-1][xCord] == 0)) && (map[yCord+1][xCord] == 0)))
				return 6;
		}
		return 0;
	}

	public static int[][] placeShip(String insertType, int xCord, int yCord, int[][] map){
		/**
		 * placeShip
		 * Diese Funktion setzt die Boote
		 * 
		 * @param insertType Der Platzierungsmodus
		 * @param xCord Die X-Koordinate
		 * @param yCord Die Y-Koordinate
		 * @param map Die Spielkarte
		 * @return Die Spielkarte mit eingefügtem Boot/en
		 */
		if(insertType.equals("W")){
			map[yCord][xCord] = 1;
            map[yCord][xCord-1] = 1;
            map[yCord][xCord+1] = 1;
		}
		if(insertType.equals("S")){
			map[yCord][xCord] = 1;
            map[yCord-1][xCord] = 1;
            map[yCord+1][xCord] = 1;
		}
		return map;
	}
	
	public static boolean errorCodeParser(int errorcode){
		/**
		 * errorCodeParser
		 * Diese Funktion parsed die Errorcodes von der Funktion checkInput
		 * 
		 * @param errorcode Der geparste Errorcode
		 * @return True oder False je nach dem ob eine Errorbedingung erfüllt wird. Wenn erfüllt wird eine Nachricht ausgegeben
		 * 
		 */
		switch(errorcode){
		case 1:
			JOptionPane.showMessageDialog(null, "Platzierungstyp muss W oder S sein!");
			return false;
		case 2:
			JOptionPane.showMessageDialog(null, "X-Koordinate muss zwischen einschließlich 2 und 9 liegen!");
			return false;
		case 3:
			JOptionPane.showMessageDialog( null, "Y-Koordinate muss zwischen einschließlich 1 und 10 liegen!");
			return false;
		case 4:
			JOptionPane.showMessageDialog(null, "X-Koordinate muss zwischen einschließlich 1 und 10 liegen!");
			return false;
		case 5:
			JOptionPane.showMessageDialog(null, "Y-Koordinate muss zwischen einschließlich 2 und 9 liegen!");
			return false;
		case 6:
			JOptionPane.showMessageDialog(null, "Das Feld ist bereits besetzt!");
			return false;
		case 0:
		default:
			return true;
			
		}
	}
	  public static void outputMap(int[][] map){
		  /**
		   * outputMap
		   * Diese Funktion gibt einfach nur die Spielkarte aus.
		   * Ich habe mich dabei an den Bildern orientiert.
		   * Es wird also auch ein Spielfeldrand eingezeichnet.
		   * 
		   * @param map
		   * @return void
		   */
		    System.out.println("------------");
		    for (int i = 0; i < map.length; i++) {
		      System.out.print("|");
		      for (int j = 0; j < map[i].length; j++) {
		        System.out.print(map[i][j]);
		      }
		      System.out.println("|");
		    }
		    System.out.println("------------");
		  }

	
	
}












