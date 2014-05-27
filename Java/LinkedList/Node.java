
public class Node {

	private Node next;
	private Node previous;
	private String information;
	
	public Node(String information){
		this.information = information;
		this.next = null;
		this.previous = null;
	}
	
	public void setNext(Node next){
		this.next = next;
	}
	
	public void setPrevious(Node previous){
		this.previous = previous;
	}
	
	public Node getNext(){
		return next;
	}
	
	public Node getPrevious(){
		return previous;
	}
	
	public String getInformation(){
		return information;
	}
	//Funktion zum Einfügen eines Nodes hinter einem Anderen
	public void addNodeAfter(Node inputNode){
		inputNode.setNext(getNext());
		if(getNext() != null){
			getNext().setPrevious(inputNode);
		}
		setNext(inputNode);
		inputNode.setPrevious(this);
	}

}
