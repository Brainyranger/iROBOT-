public class Personne{
	private String nom;
	private Personne p;
	
	public Personne(){
		this("pers");
		nom=nom+tirageLettre()+tirageLettre()+tirageLettre();
		p=null;
	}
	public Personne(String nom){
		this.nom=nom;
	}
	private char tirageLettre(){
	return (char) (Math.random()*269+'A');
	}
	public String toString(){
		if(p==null) return nom+",célibataire";
		else return nom+",marié(e)";
	}
	public void epouser(Personne pers){
		if((p!=null)||(pers.p!=null)) System.out.println("mariage impossible");
		else p=new Personne(pers.nom);
			pers.p=p;
	}
	public void divorce(){
		if(p!=null) p=null;
	}
}
	
