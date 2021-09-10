package newestPackage;

public class nonInheritence {
    public static void main(String [] args){
        Ogrenci ulvi = new Ogrenci("Ulvi",20,34324,1034);
        System.out.println(ulvi);
    }
}

class Personel{

    private String isim;
    private long tcKimlik;
    private int yas;

    public Personel(){
        isim = "Henüz atanmadı";
        tcKimlik = 0;
        yas = 18;
    }

    public Personel(String isim, long tcKimlik, int yas){
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
        return "Ad: "+isim+" Tc Kimlik: "+tcKimlik+"Yaş: "+yas;
    }
}

class Ogrenci{

    private String isim;
    private int yas;
    private long tcKimlik;
    private int okulNo;

    public Ogrenci(){
        isim = "Henüz atanmadı";
        yas = 18;
        tcKimlik = 0;
        okulNo = 5000;
    }

    public Ogrenci(String isim, int yas, long tcKimlik, int okulNo){
        this.isim = isim;
        setYas(yas);
        this.tcKimlik = tcKimlik;
        this.okulNo = okulNo;
    }

    public String getIsim() {
        return isim;
    }

    public void setIsim(String isim) {
        this.isim = isim;
    }

    public int getYas() {
        return yas;
    }

    public void setYas(int yas) {
        if(yas >= 7) {
            this.yas = yas;
        }else this.yas = 7;
    }

    public long getTcKimlik() {
        return tcKimlik;
    }

    public void setTcKimlik(long tcKimlik) {
        this.tcKimlik = tcKimlik;
    }

    public int getOkulNo() {
        return okulNo;
    }

    public void setOkulNo(int okulNo) {
        this.okulNo = okulNo;
    }

    @Override
    public String toString() {
        return "Ad: "+isim+" Tc Kimlik: "+tcKimlik+" Yaş: "+yas+" Okul No: "+okulNo;
    }
}
