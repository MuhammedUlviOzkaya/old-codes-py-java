package newestPackage;

public class BindingTypes {
    public static void main(String[] args){
/*        UstSinif.adiniSoyleStatic();
        AltSinif.adiniSoyleStatic();

        UstSinif usObject = new UstSinif();
        usObject.adiniSoyleStatic();

        AltSinif asObject = new AltSinif();
        asObject.adiniSoyleStatic();


        UstSinif ustSinif = new AltSinif();
        ustSinif.adiniSoyleStatic();
*/
        UstSinif ustSinif = new UstSinif();
        ustSinif.adiniSoyle();

        AltSinif altSinif = new AltSinif();
        altSinif.adiniSoyle();

        UstSinif ustSinif1 = new AltSinif();
        ustSinif1.adiniSoyle();





    }

}

class UstSinif{

    public static void adiniSoyleStatic(){
        System.out.println("Üst sınıfın static adını söyle metodu çağrıldı.");
    }

    public void adiniSoyle(){
        System.out.println("Üst sınıfın adını söyle metodu çağrıldı.");
    }

}

class AltSinif extends UstSinif{

    public static void adiniSoyleStatic(){
        System.out.println("Alt sınıfın static adını söyle metodu çağrıldı.");
    }

    @Override
    public void adiniSoyle() {
        System.out.println("Alt sınıfın adını söyle metodu çağrıldı.");
    }
}
