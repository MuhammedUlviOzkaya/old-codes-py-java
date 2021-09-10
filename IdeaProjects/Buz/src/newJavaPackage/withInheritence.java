package newJavaPackage;

public class withInheritence {
    public static void main(String [] args){
        Personel mudur = new Personel("Kaan",213124,16,"Müdür");
        System.out.println(mudur);

        Ogrenci ulvi = new Ogrenci("Ulvi",12341345,20,560);
        System.out.println(ulvi);

        MezunOgrenci o1 = new MezunOgrenci("Türkan",1435246,25,272,"Zeytin Eczanesi");
        System.out.println(o1);


    }
}

class Kisi{

    private String isim;
    private long tcKimlik;
    private int yas;

    public Kisi(){
        isim = "Henüz atanmadı";
        tcKimlik = 0;
        yas = 18;
    }

    public Kisi(String isim, long tcKimlik, int yas){
        this.isim = isim;
        this.tcKimlik = tcKimlik;
        setYas(yas);
    }

    public String getIsim(){
        return isim;
    }

    public void setIsim(String veri){
        this.isim = veri;
    }

    public long getTcKimlik(){
        return tcKimlik;
    }

    public void setTcKimlik(long veri){
        this.tcKimlik = veri;
    }

    public int getYas(){
        return yas;
    }

    public void setYas(int veri){
        if(veri >= 18) {
            this.yas = veri;
        }else this.yas = 18;
    }

    @Override
    public String toString() {
        return "Ad: "+isim+" Tc Kimlik: "+tcKimlik+" Yaş: "+yas;
    }
}

class Personel extends Kisi{

    private String pozisyon;

    public Personel(String isim, long tcKimlik, int yas, String pozisyon) {
        super(isim, tcKimlik, yas);
        this.pozisyon = pozisyon;
    }

    public String getPozisyon() {
        return pozisyon;
    }

    public void setPozisyon(String pozisyon) {
        this.pozisyon = pozisyon;
    }

    @Override
    public String toString() {
        return "Personel adı: "+getIsim()+" Tc Kimlik: "+getTcKimlik()+" Yaş: "+getYas()+" Pozisyon: "+getPozisyon();
    }
}

class Ogrenci extends Kisi{
    private int ogrenciNo;

    public int getOgrenciNo() {
        return ogrenciNo;
    }

    public void setOgrenciNo(int ogrenciNo) {
        this.ogrenciNo = ogrenciNo;
    }

    public Ogrenci(String isim, long tcKimlik, int yas, int ogrenciNo) {
        super(isim,tcKimlik,yas);
        this.ogrenciNo = ogrenciNo;
    }

    @Override
    public String toString() {
        return "Öğrenci Adı: "+getIsim()+" Tc Kimlik: "+getTcKimlik()+" Yaş: "+getYas()+" Öğrenci No: "+ogrenciNo;
    }
}

class MezunOgrenci extends Ogrenci{

    private String calismaYeri;

    public MezunOgrenci(String isim, long tcKimlik, int yas, int ogrenciNo, String calismaYeri) {
        super(isim, tcKimlik, yas, ogrenciNo);
        this.calismaYeri = calismaYeri;
    }


    public String getCalismaYeri() {
        return calismaYeri;
    }

    public void setCalismaYeri(String calismaYeri) {
        this.calismaYeri = calismaYeri;
    }

    @Override
    public String toString() {
        return "Öğrenci Adı: "+getIsim()+" Tc Kimlik: "+getTcKimlik()+" Yaş: "+getYas()+" Öğrenci No: "+getOgrenciNo()+" Çalışma Yeri: "+getCalismaYeri();
    }
}
