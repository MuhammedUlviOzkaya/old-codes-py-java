package newestPackage;

public class Polymorphism {

    public static void main(String[] args){
        Hayvan h1 = new Hayvan();
        Kopek kopek1 = new Kopek("Kangal");
        Kedi kedi1 = new Kedi("Tekir");

        adiniSoyle(h1);
        adiniSoyle(kedi1);
        adiniSoyle(kopek1);


    }


    public static void adiniSoyle(Hayvan hayvan){
        hayvan.adiniSoyle();

    }





}

class Hayvan{
    private int ayakSayisi;

    public int getAyakSayisi(){
        return ayakSayisi;
    }

    public void setAyakSayisi(int sayi){
        this.ayakSayisi = sayi;
    }

    public void adiniSoyle(){
        System.out.println("Ben hayvan sınıfı nesnesiyim.");
    }

}

class Kopek extends Hayvan{

    private String tur;

    public Kopek(String tur){
        setTur(tur);
        setAyakSayisi(4);
    }

    public String getTur(){
        return tur;
    }

    public void setTur(String tur){
        this.tur = tur;
    }

    @Override
    public void adiniSoyle() {
        System.out.println("Ben bir köpek nesnesiyim.");
    }
}

class Kedi extends Hayvan{

    private String cinsi;

    public Kedi(String cins){
        setAyakSayisi(4);
        setCinsi(cins);

    }

    public String getCinsi(){
        return cinsi;
    }

    public void setCinsi(String cins){
        this.cinsi = cins;
    }

    @Override
    public void adiniSoyle() {
        System.out.println("Ben bir kedi nesnesiyim.");
    }
}