package newestPackage;

import java.util.ArrayList;

public class Televizyon {
    private String marka;
    private String boyut;
    private ArrayList<Kanal> kanallar;
    private boolean acik;
    private int ses;
    private int aktifKanal;

    public Televizyon(String marka, String boyut){
        this.marka = marka;
        this.boyut = boyut;
        ses = 10;
        kanallar = new ArrayList<>();
        kanallariOlustur();
        this.acik = false;
        aktifKanal = 1;
    }

    public void sesArttir(){
        if(ses < 20 && acik == true){
            ses++;
            System.out.println("Ses seviyesi: "+ses);
        }else{
            System.out.println("Ses zaten maksimum seviyede ya da TV kapalı.");
        }
    }

    public void sesAzalt(){
        if(ses >= 0){
            ses--;
            System.out.println("Ses seviyesi: "+ses);
        }else{
            System.out.println("Ses zaten minimum seviyede.");
        }
    }

    public void aktifKanaliGoster(){
        System.out.println("Aktif Kanal: "+kanallar.get(aktifKanal).kanalBilgisiniGoster());
    }

    public void tvAc(){
        if(acik == false){
            acik = true;
            System.out.println("TV açıldı");
        }else{
            System.out.println("TV zaten açık");
        }
    }

    public void tvKapat(){
        if(acik == true){
            acik = false;
            System.out.println("TV kapandı");
        }else{
            System.out.println("TV zaten kapalı");
        }
    }

    private void kanallariOlustur() {
        HaberKanali cnn = new HaberKanali("Cnn",1,"Genel Haber");
        kanallar.add(cnn);
        HaberKanali ntvSpor = new HaberKanali("NTV Spor",3,"Spor Haberleri");
        kanallar.add(ntvSpor);
        MuzikKanali dreamTurk = new MuzikKanali("Dream Türk",2,"Yerli");
        kanallar.add(dreamTurk);
        MuzikKanali nr1 = new MuzikKanali("Number One",4,"Yabancı");
        kanallar.add(nr1);
    }

    public void kanalDegistir(int acilmasiIstenenKanal){
        if(acik){
            if(acilmasiIstenenKanal != aktifKanal){

                if(acilmasiIstenenKanal <= kanallar.size() && acilmasiIstenenKanal >= 0){
                    aktifKanal = acilmasiIstenenKanal;
                    System.out.println(aktifKanal+". kanaldasınız."+kanallar.get(aktifKanal-1).kanalBilgisiniGoster());
                }else{
                    System.out.println("Geçerli bir kanal numarası giriniz.");
                }


            }else{
                System.out.println("Zaten "+aktifKanal+". kanaldasınız.");
            }
        }else{
            System.out.println("Önce tv yi açınız.");
        }
    }

    public String getMarka(){
        return this.marka;
    }

    public void setMarka(String marka){
        this.marka = marka;
    }

    public String getBoyut(){
        return this.boyut;
    }

    public void setBoyut(String boyut){
        this.boyut = boyut;
    }

    @Override
    public String toString() {
        return "Marka: "+marka+" Boyut: "+boyut+" olan tv oluşturuldu.";
    }
}
