package newestPackage;

public class SoyutSinifKavrami {

    public static void main(String [] args){
    GeometrikSekil kare = new Kare(5);
    GeometrikSekil dikdortgen = new Dikdortgen(6,10);
    GeometrikSekil daire = new Daire(9);

    kare.alanHesapla();
    dikdortgen.alanHesapla();
    daire.alanHesapla();

    alanlariKarsilastir(kare,dikdortgen);





    }

    public static void alanlariKarsilastir(GeometrikSekil gs1, GeometrikSekil gs2){
        if(gs1.getHesaplananAlan() > gs2.getHesaplananAlan()){
            System.out.println("Birinci parametredeki nesnenin alanı ikinci parametredeki nesnenin alanından büyüktür.");
        } else if(gs1.getHesaplananAlan() < gs2.getHesaplananAlan()){
            System.out.println("Birinci parametredeki nesnenin alanı ikinci parametredeki nesnenin alanından küçüktür.");
        }else{
            System.out.println("Nesnelerin alanları eşittir.");
        }
    }


}

abstract class GeometrikSekil{

    private int birinciKenar;
    private int hesaplananAlan;

    public int getHesaplananAlan() {
        return hesaplananAlan;
    }

    public void setHesaplananAlan(int hesaplananAlan) {
        this.hesaplananAlan = hesaplananAlan;
    }

    abstract public void cevreHesapla();

    abstract public void alanHesapla();


    public int getBirinciKenar(){
        return this.birinciKenar;
    }

    public void setBirinciKenar(int birinciKenar){
        this.birinciKenar = birinciKenar;
    }



}

class Kare extends GeometrikSekil{

    public Kare(int kenar) {
        this.setBirinciKenar(kenar);
    }

    @Override
    public void cevreHesapla() {
        System.out.println("Karenin çevresi: "+getBirinciKenar()*4);
    }

    @Override
    public void alanHesapla() {
        setHesaplananAlan(getBirinciKenar()*getBirinciKenar());
        System.out.println("Karenin alanı: "+ getHesaplananAlan());
    }
}

class Dikdortgen extends GeometrikSekil{

    private int ikinciKenar;

    public Dikdortgen(int birinciKenar, int ikinciKenar) {
        setBirinciKenar(birinciKenar);
        this.ikinciKenar = ikinciKenar;
    }

    public int getIkinciKenar() {
        return ikinciKenar;
    }

    public void setIkinciKenar(int ikinciKenar) {
        this.ikinciKenar = ikinciKenar;
    }

    @Override
    public void cevreHesapla() {
        System.out.println("Dikdörtgenin çevresi: "+2*(getBirinciKenar() + ikinciKenar));
    }

    @Override
    public void alanHesapla() {
        setHesaplananAlan(getBirinciKenar()*ikinciKenar);
        System.out.println("Dikdörtgenin alanı: "+getHesaplananAlan());
    }
}

class Daire extends GeometrikSekil{


    public Daire(int yariCap) {
        setBirinciKenar(yariCap);
    }

    @Override
    public void cevreHesapla() {
        System.out.println("Dairenin çevresi: "+2*3.14*getBirinciKenar());
    }

    @Override
    public void alanHesapla() {
        setHesaplananAlan(3*getBirinciKenar()*getBirinciKenar());
        System.out.println("Dairenin alanı: "+getHesaplananAlan());
    }
}
