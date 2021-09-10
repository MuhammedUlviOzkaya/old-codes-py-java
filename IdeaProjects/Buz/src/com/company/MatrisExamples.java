package com.company;
import java.util.Scanner;

public class MatrisExamples {
    public static void main(String [] args){
        Scanner data = new Scanner(System.in);
        System.out.println("Öğrenci sayısını girin: ");
        int ogrenciSayisi = data.nextInt();

        System.out.println("Toplam soru sayısını girin: ");
        int soruSayisi = data.nextInt();

        char[][] tumCevaplar = new char[ogrenciSayisi][soruSayisi];
        char cevapAnahtari[] = new char[soruSayisi];


        cevapOlustur();
        ogrenciCevaplariniYerlestir(tumCevaplar);
        cevapAnahtariOlustur(cevapAnahtari);
        ogrencileriDegerlendir(cevapAnahtari,tumCevaplar);





    }
    public static void ogrencileriDegerlendir(char cevapAnahtari[], char tumCevaplar[][]){
        for(int satir = 0; satir < tumCevaplar.length; satir++){
            int dogruSayisi = 0;
            for(int sutun = 0; sutun< tumCevaplar[satir].length; sutun++){
                if(tumCevaplar[satir][sutun] == cevapAnahtari[sutun]){
                    dogruSayisi++;

                }
            }
            System.out.println(satir+" indexindeki öğrencinin doğru sayısı: "+dogruSayisi);

        }




    }
    public static void cevapAnahtariOlustur(char cevapAnahtari[]){
        for(int i = 0; i<cevapAnahtari.length; i++){
            cevapAnahtari[i] = cevapOlustur();

        }



    }
    public static void ogrenciCevaplariniYerlestir(char tumCevaplar[][]){
        for(int satir = 0; satir<tumCevaplar.length; satir++){

            for(int sutun = 0; sutun< tumCevaplar[satir].length; sutun++ ){

                tumCevaplar[satir][sutun] = cevapOlustur();



            }


        }



    }
    public static char cevapOlustur(){
        int rastgeleSayi = 65 + (int)(Math.random()*5);
        char uretilenSecenek = (char)rastgeleSayi;

        return uretilenSecenek;




    }
}
