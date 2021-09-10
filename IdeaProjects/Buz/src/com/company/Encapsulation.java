package com.company;



public class Encapsulation {
    public static void main(String[] args) {
        Ogrenciler dizi [] = new Ogrenciler[100];



        for(int i = 0; i<100; i++){
            int rastgeleID = (int)(Math.random()*10000);
            int rastgeleNot = (int)(Math.random()*100);

            Ogrenciler gecici = new Ogrenciler(rastgeleID,rastgeleNot);
            dizi[i] = gecici;

        }

        notlariSirala(dizi);
        for(int i = 0; i< dizi.length; i++){
            dizi[i].ogrenciYazdir();
        }









    }

    public static void notlariSirala(Ogrenciler [] dizi){
        for(int i = 0; i<dizi.length; i++){
            int maxNot = dizi[i].getogrenciNot();
            int maxNotIndex = i;

            for(int j = i+1; j<dizi.length; j++){
                if(maxNot < dizi[j].getogrenciNot()){
                    maxNot = dizi[j].getogrenciNot();
                    maxNotIndex = j;


                }


            }
            if(maxNotIndex != i){
                dizi[maxNotIndex] = dizi[i];
                dizi[i].setogrenciNot(maxNot);
            }


        }

    }

}

class Ogrenciler{
    private int id;
    private int ogrenciNot;

    public Ogrenciler(int id, int not){
        this.id = id;
        this.ogrenciNot = not;


    }


    public int getId(){
        return id;
    }

    public void setId(int id){
        this.id = id;
    }

    public int getogrenciNot(){
        return ogrenciNot;
    }

    public void setogrenciNot(int not){
        this.ogrenciNot = not;
    }

    public void ogrenciYazdir(){
        System.out.println("Öğrenci id: "+id+" Öğrenci not: "+ogrenciNot);
    }




}
