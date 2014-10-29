/**
 * Just a simple example for double chained lists
 * @author Christian Rebischke
 *
 */


public class LinkedList {

	public static void main(String[] args) {
		//Nodes erstellen
		Node first = new Node("First Element");
		Node second = new Node("Second Element");
		Node third = new Node("Third Element");
		//Nodes verketten: Zweites Element hinter dem Ersten einfügen
		//Drittes element hinter dem Ersten einfügen
		first.addNodeAfter(second);
		first.addNodeAfter(third);
		//Ausgabe über next-Element
		System.out.println(first.getInformation());
		System.out.println(first.getNext().getInformation());
		System.out.println(first.getNext().getNext().getInformation());

	}

}
