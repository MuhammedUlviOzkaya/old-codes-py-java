package newJavaPackage;

public class Composition {
    public static void main(String[] args){
    Araba myAraba = new Araba();
        System.out.println(myAraba.renk);
        System.out.println(myAraba.marka);
        System.out.println(myAraba.uretimYili);
        System.out.println(myAraba.arabaMotoru.isim);
        System.out.println(myAraba.arabaMotoru.beygirGucu);


    }

}

class Motor{
    public String isim;
    public int beygirGucu;

    public Motor(){
        isim = "BMW";
        beygirGucu = 150;
        System.out.println(isim+" isimli ve "+beygirGucu+" beygir güçlü motor oluşturuldu.");
    }

    public void motoruCalistir(){
        System.out.println("Motor çalıştırılıyor...");
    }

    public void motoruDurdur(){
        System.out.println("Motor durduruluyor.");
    }



}

class Araba{
    public Motor arabaMotoru;
    public String renk;
    public String marka;
    public int uretimYili;

    public Araba(){
        arabaMotoru = new Motor();
        renk = "Sarı";
        marka = "Merso";
        uretimYili = 2019;
        System.out.println(renk+" renkli, "+uretimYili+" model "+marka+" marka araba oluşturuldu.");

    }

    public void hareketeGec(){
        System.out.println("Araba harekete geçiyor...");
    }

    public void dur(){
        System.out.println("Araba duruyor...");
    }



}
