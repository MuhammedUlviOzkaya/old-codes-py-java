package newJavaPackage;

public class Inheritence {
    public static void main(String[] args){
        Dikdortgen d1 = new Dikdortgen(3,5);
        GeometrikSekil gs1 = new GeometrikSekil(7);
        Kare k1 = new Kare(9);

        alaniGoster(d1);
        alaniGoster(gs1);
        alaniGoster(k1);














    }

    public static void alaniGoster(GeometrikSekil sekil){
        if(sekil instanceof Kare){
            Kare gecici = (Kare)sekil;
            sekil.alanHesapla();
            System.out.println("Kare içindeki alan hesapla çağrıldı.");
        }else if(sekil instanceof Dikdortgen){
            Dikdortgen gecici = (Dikdortgen)sekil;
            gecici.alanHesapla();
            System.out.println("Dikdörtgen içindeki alan hesapla çağrıldı.");
        }else{
            sekil.alanHesapla();
            System.out.println("Geometrik şekil içindeki alan hesapla çağrıldı.");

        }

    }

}

class GeometrikSekil{
    private int en;
    private int boy;

    public GeometrikSekil(int en, int boy){
        this.en = en;
        this.boy = boy;
    }

    public GeometrikSekil(){

    }

    public GeometrikSekil(int en){
        this.en = en;
    }

    public int getEn(){
        return en;
    }

    public void setEn(int en){
        this.en = en;
    }

    public int getBoy(){
        return boy;
    }

    public void setBoy(int boy){
        this.boy = boy;
    }

    public void alanHesapla(){
        System.out.println("Alan= "+en*boy);
    }

    public void cevreHesapla(){
        System.out.println("Çevre= "+(2*(en+boy)));
    }

    @Override
    public String toString() {
        return "En: "+en+" boy: "+boy;
    }
}

class Dikdortgen extends GeometrikSekil{

    public Dikdortgen(int en, int boy){
        super(en,boy);
    }

    public Dikdortgen(int en){
        setEn(en);
    }



    public void dikdortgeniYazdir(){
        System.out.println("Geometrik şeklin eni: "+getEn()+" ve boyu: "+getBoy());
        alanHesapla();
        cevreHesapla();
    }
    @Override
    public String toString() {
        return "Dikdörtgenin eni: "+getEn()+" boyu: "+getBoy();
    }



}

class Kare extends Dikdortgen{


    public Kare(int en) {
        super(en);
        setBoy(en);
    }
}
