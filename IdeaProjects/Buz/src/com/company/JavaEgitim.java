package com.company;


import java.util.Scanner;

public class JavaEgitim {
    public static void main(String[] args) {
       /*

        int yaricap = 7;
        int daireninCevresi = 2*3*yaricap;
        Scanner input=new Scanner(System.in);


        System.out.println("Alanın hesaplamak istediğiniz dairenin yarıçapını girin: ");
        int kullanicininYaricapi = input.nextInt();

        System.out.println("Dairenin alanı: "+2*3*kullanicininYaricapi);








        Scanner input = new Scanner(System.in);
        int random1 = (int)(System.currentTimeMillis()%10);
        int random2 = (int)(System.currentTimeMillis()/10 %10);
        System.out.println(random1+ "+"+random2+ "= sonuç gir");
        int sonuc = input.nextInt();
        System.out.println( "=" +sonuc );
        System.out.println(random1+random2==sonuc);


        Scanner input = new Scanner(System.in);
        System.out.println("bir sayı gir canımın içi");
        int sayi1 = input.nextInt();
        System.out.println("girdiğiniz için teşekkürler");
        if (sayi1 %2 == 0){
            System.out.println("girdiğiniz sayı " +sayi1+ " 2'ye tam bölünür.");
        }
        else if (sayi1 %3 == 0){
            System.out.println("girdiğiniz sayı " +sayi1+ " 3e tam bölünür");


        }
        else {
            System.out.println("girdiğiniz sayı " +sayi1+ " sayınız piç");

        }

        Scanner input = new Scanner(System.in);

        int sayi;

        sayi = 7/2;
        System.out.println("Sayı: "+sayi);


        sayi = 10;
        System.out.println("Sayının yeni hali: "+sayi);


        String kelime = "Muhammed Ulvi Özkaya";
        System.out.println(kelime);

        String kelime2 = "mustafa tarık seni seviyor"; // tırnak işareti kullan
        System.out.println(kelime2);
        char karaktersiz = '&';

        char karakter = 'A';
        char karakter2 = '%';


        boolean asd = true;

        System.out.println(asd);

        asd = false;
        System.out.println(asd);

        sayi++;
        ++sayi;
        System.out.println("Sayımız şuan "+sayi);

        sayi += 5; //sayi = sayi + 5
        System.out.println(sayi);
        sayi += 3;
        if(sayi != 20){
            System.out.println("Sayı 20'ye eşit değil.");
        }else{
            System.out.println("Sayı 20'ye eşit.");
        }

        if(sayi>=15 && sayi<=40){
            System.out.println("sayı 20 işte uzatma");
        }

        if(!(sayi<12 || (sayi<40 && sayi%5==1))){
            System.out.println("sayımız heycanlı" );

        }
        else{
            System.out.println("sakin sayı");
        }


                String qwert ="ihtiyacımız var";
        System.out.println(qwert.length());
        System.out.println(qwert.toUpperCase());
        qwert= qwert.toUpperCase();

        System.out.println(qwert.toLowerCase());

        String nobet = "eczane zeytin \"bugün\" nöbetçi eczane";  //tarık heyyavrum
        System.out.println(nobet);                                //tarık heyyavrum
        System.out.println("gs 4 yıldızlı takım. \nvay be");      //tarık heyyavrum
                                                                  //tarık heyyavrum
        String armut = "10";                                      //tarık heyyavrum
        String elma = "29";                                       //tarık heyyavrum
         String karpuz = armut + elma;                            //tarık heyyavrum
        System.out.println(armut+elma);                           //tarık heyyavrum
        System.out.println(karpuz);                               //tarık heyyavrum
        System.out.println(Math.max(101,509));                    //tarık heyyavrum
        int q = -23;                                              //tarık heyyavrum
                int absq = Math.abs(q);                           //tarık heyyavrum
        System.out.println(absq);                                 //tarık heyyavrum
                                                                  //tarık heyyavrum
                                                                  //tarık heyyavrum
        */

        Scanner input = new Scanner(System.in);
        System.out.println("saat gir");
        int saat = input.nextInt();
        if (saat < 12) {
            System.out.println("günaydın");

        } else if (saat < 18) {
            System.out.println("iyi günler");

        } else {
            System.out.println("iyi akşamlar");


        }

    }
}







