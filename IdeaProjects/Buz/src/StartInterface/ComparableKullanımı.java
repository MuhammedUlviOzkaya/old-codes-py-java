package StartInterface;

import java.util.Arrays;

public class ComparableKullanımı {

    public static void main(String[] args){

        Ogrenci ogr1 = new Ogrenci(3,"ulvi");
        Ogrenci ogr2 = new Ogrenci(7,"asude");
        Ogrenci ogr3 = new Ogrenci(9,"türkan");

        Ogrenci[] ogrenciler = {ogr1,ogr2,ogr3};

        System.out.println("Sıralanmadan önce: ");
        for(Ogrenci nesneler:ogrenciler){
            System.out.println(nesneler);
        }

        Arrays.sort(ogrenciler);

        System.out.println("Sıralanmadan sonra: ");

        for(Ogrenci nesneler:ogrenciler){
            System.out.println(nesneler);
        }





    }

}

class Ogrenci implements Comparable<Ogrenci>{
    int id;
    String ad;

    public Ogrenci(int id, String ad){
        this.id = id;
        this.ad = ad;
    }

    @Override
    public String toString() {
        return "ad: "+ad+" id: "+id;
    }

    @Override
    public int compareTo(Ogrenci ogrenci) {
        if(this.id < ogrenci.id){
            return 1;
        }else if(this.id > ogrenci.id){
            return -1;
        }else return 0;
    }
}
