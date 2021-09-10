package newJavaPackage;

public class BankAccount {
    public static void main(String[] args){
        BankaHesap hesapBuz = new BankaHesap(123,740);
        BankaHesap hesapUlvi = new BankaHesap(124,680);

        hesapBuz.paraYatir(100);
        int bakiyem = hesapBuz.getHesapBakiye();
        System.out.println(bakiyem);

        hesapUlvi.paraCek(170);

        hesapBuz.paraCek(150);

        hesapBuz.paraYatir(10000);

        BankaHesap.ozetGoster();

        hesapBuz.kiyasla(hesapUlvi);
        hesapUlvi.kiyasla(hesapBuz);

        hesapBuz.setHesapNo(1710);

        hesapBuz.kiyasla(hesapUlvi);



    }
}

class BankaHesap{
    private int hesapNo;
    private int hesapBakiye;
    private static int tumBankaBakiyesi;
    private static int tumHesapSayisi = 0;
    private static int operasyonSayisi = 0;

    public BankaHesap(int hesapNo, int hesapBakiye){
        this.hesapNo = hesapNo;
        this.hesapBakiye = hesapBakiye;
        tumBankaBakiyesi += hesapBakiye;
        tumHesapSayisi++;
    }



    public int getHesapNo(){
        return hesapNo;
    }

    public void setHesapNo(int hesapNo){
        this.hesapNo = hesapNo;
    }

    public int getHesapBakiye(){
        return hesapBakiye;
    }

    public void setHesapBakiye(int hesapBakiye){
        this.hesapBakiye = hesapBakiye;
    }

    public void paraYatir(int paraMiktari){
        this.hesapBakiye += paraMiktari;
        operasyonSayisi++;
        tumBankaBakiyesi += paraMiktari;
    }

    public void paraCek(int paraMiktari){
        if(hesapBakiye >= paraMiktari){
            this.hesapBakiye -= paraMiktari;
            operasyonSayisi++;
            tumBankaBakiyesi -= paraMiktari;
        }else{
            System.out.println("Yetersiz Bakiye");
        }
    }

    public void kiyasla(BankaHesap kiyaslanacakHesap){
        if(this.hesapBakiye < kiyaslanacakHesap.getHesapBakiye()){
            System.out.println(this.hesapNo+" no lu hesap "+kiyaslanacakHesap.getHesapNo()+" no lu hesaptan daha az bakiyeye sahiptir.");
        }else if(this.hesapBakiye > kiyaslanacakHesap.getHesapBakiye()){
            System.out.println(this.hesapNo+" no lu hesap "+kiyaslanacakHesap.getHesapNo()+" no lu hesaptan daha fazla bakiyeye sahiptir.");
        }else{
            System.out.println("2 hesabın bakiyeleri eşittir.");
        }

    }

    public static void ozetGoster(){
        System.out.println("Bankadaki hesap sayısı: "+tumHesapSayisi);
        System.out.println("Bankadaki toplam para miktari(TL): "+tumBankaBakiyesi);
        System.out.println("Bankada yapılan tüm işlemlerin sayısı: "+operasyonSayisi);
    }


}
