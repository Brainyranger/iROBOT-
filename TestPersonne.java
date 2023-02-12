public class TestPersonne{
	public static void main(String[] args){
		Personne p1=new Personne();
		Personne p2=new Personne();
		Personne p3=new Personne();
		System.out.println(p1.toString());
		System.out.println(p2.toString());
		System.out.println(p3.toString());
		p1.epouser(p2);
		System.out.println("le mariage de"+p1.toString()+"et de "+p2.toString());
		System.out.println(p1.toString());
		System.out.println(p2.toString());
		p1.epouser(p3);
		p1.divorce();
		p2.divorce();
		System.out.println(p1.toString());
		System.out.println(p2.toString());
	}
}
	
		
