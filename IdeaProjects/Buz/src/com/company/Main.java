package com.company;

import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String a = "Ulvi";
        System.out.println(a.charAt(0));
        System.out.println(a.charAt(3));
        /*
        Scanner gun = new Scanner(System.in);
        System.out.println("Kaç gün sonra buluşacağız? :");
        int gunDegeri = gun.nextInt();
        switch (gunDegeri){                   
            case 1:
                System.out.println("Pazartesi"); break;
            case 2:
                System.out.println("Salı"); break;
            case 3:
                System.out.println("Çarşamba"); break;
            case 4:
                System.out.println("Perşembe"); break;
            case 5:
                System.out.println("Cuma"); break;
            case 6:
                System.out.println("Cumartesi"); break;
            case 7:
                System.out.println("Pazar"); break;

            default:
                System.out.println("Haftanın "+gunDegeri%7+". günü buluşacağız.");
        }
//
        System.out.println("Bir kelime giriniz: ");
        Scanner harf = new Scanner(System.in);
    String a = harf.next();
        System.out.println("Girdiğiniz cümlenin ilk kelimesi: "+a);

        Scanner input = new Scanner(System.in);
        int a = 3;
        System.out.println("Değerimiz: "+a);
        System.out.println("Rint ile: "+ Math.rint(a));
        System.out.println("Ceil ile: "+ Math.ceil(a));
        System.out.println("Floor ile: "+ Math.floor(a));
        System.out.println("Mutlak değer ile: "+ Math.abs(a));

        Math.random()*(üst sınır +1) = Üst sınıra kadar random sayılar üst sınır dahil 0 da dahil
        Math.random()* üst sınır +1 = Üst sınıra kadar random sayılar üst sınır dahil 0 dahil değil

//

        int cekilisSayisi = (int)(Math.random()*99 + 1);
        System.out.println("Tahmin sayınızı giriniz: ");
        int tahminSayisi;
        Scanner cekilis = new Scanner(System.in);
        tahminSayisi = cekilis.nextInt();
        if(tahminSayisi==cekilisSayisi){
            System.out.println("Sayıyı tamamen bildiniz ve 10.000 TL ödülü kazandınız!");
            System.out.println("Sizin tahmininiz: "+ tahminSayisi + " Şanslı sayı: "+cekilisSayisi);
        }else if(cekilisSayisi/10 == tahminSayisi % 10 && cekilisSayisi%10 == tahminSayisi/10){
            System.out.println("Sayının rakamlarını bildiniz ve 5.000 TL kazandınız!");
            System.out.println("Sizin tahmininiz: "+ tahminSayisi + " Şanslı sayı: "+ cekilisSayisi);
        }else if(cekilisSayisi/10 == tahminSayisi/10 || cekilisSayisi%10 == tahminSayisi/10 || cekilisSayisi/10 == tahminSayisi%10 || cekilisSayisi%10 == tahminSayisi%10){
            System.out.println("Sayının 1 rakamını bildiniz ve 1.000 TL ödül kazandınız!");
            System.out.println("Sizin tahmininiz: "+tahminSayisi+" Şanslı sayı: "+cekilisSayisi);
        }else{
            System.out.println("Şanslı Sayı: "+cekilisSayisi+ " Tekrar Deneyin!");
        }
//
        Scanner sayilar = new Scanner(System.in);
        System.out.println("Üçgenin kenar ölçülerini giriniz");
        System.out.println("Birinci kenar: ");
        int kenar1 = sayilar.nextInt();
        System.out.println("İkinci kenar: ");
        int kenar2 = sayilar.nextInt();
        System.out.println("Üçüncü kenar: ");
        int kenar3 = sayilar.nextInt();
        if(kenar1 == kenar2 && kenar1 == kenar3){
            System.out.println("Üçgeniniz bir eşkenar üçgendir.");
        }else if((kenar1 == kenar2 && kenar1 != kenar3) || (kenar1 == kenar3 && kenar2 != kenar3) || (kenar2 == kenar3 && kenar2 !=kenar1)){
            System.out.println("Üçgeniniz bir ikizkenar üçgendir.");
        }else {
            System.out.println("Üçgeniniz bir çeşitkenar üçgendir.");
        }
//
        for(int i = 0;i<=4;i++){
            System.out.println("Muhammed Ulvi Özkaya");
        }
        int sayac = 0;
        while(sayac<5){
            System.out.println(sayac+". Muhammed Ulvi Özkaya");
            sayac++;
        }
        int sayac2 = 0;
        do{
            System.out.println("Muhammed Ulvi Özkaya "+sayac2);
            sayac2++;
        } while(sayac2<5);
//
        int toplam = 0;
        for(int i = 0;i<=100;i++){
            toplam = toplam + i;
        }
        System.out.println("1'den 100'e kadar sayıların toplamı: "+toplam);
//
        for(int i = 1;i<=10;i++){
            System.out.print(i);
            if(i!=10){
                System.out.print(", ");
            }
        }

        Scanner sayilar = new Scanner(System.in);
        System.out.println("Faktöriyeli hesaplanacak sayıyı giriniz: ");
        int sayi = sayilar.nextInt();
        int sayac = 1, faktoriyel = 1;
        while(sayac<=sayi){
            faktoriyel = faktoriyel*sayac;
            sayac++;
        }
        System.out.println("Girdiğiniz "+sayi+" sayısının faktöriyeli: "+faktoriyel);

        int sistemSayisi = (int)(Math.random()*100+1);
        Scanner input = new Scanner(System.in);
        int tahminSayisi=0;
        int denemeSayisi = 0;


        while (tahminSayisi != sistemSayisi) {
            System.out.println("Bir sayı giriniz. Şimdiye kadarki deneme sayısı: "+denemeSayisi);
            tahminSayisi = input.nextInt();
            denemeSayisi++;
            if(sistemSayisi<tahminSayisi){
                System.out.println("Biraz düş");
            }else if(sistemSayisi>tahminSayisi){
                System.out.println("Biraz çık");
            }
        }
        System.out.println("Tebrikler! Deneme sayınız: "+denemeSayisi);
 //
        Scanner sayilar = new Scanner(System.in);
        System.out.println("Birinci sayıyı girin:");
        int sayi1 = sayilar.nextInt();
        System.out.println("İkinci sayıyı girin:");
        int sayi2 = sayilar.nextInt();
        int ebob = 1;
        int kontrol = 2;

        while(kontrol<=sayi1 && kontrol<=sayi2){
            if(sayi1 % kontrol == 0 && sayi2 % kontrol == 0){
                ebob = kontrol;
            }
            kontrol++;
        }
        if(ebob == 1){
            System.out.println(sayi1+" ve "+sayi2+" aralarında asaldır.");
        }else{
            System.out.println(sayi1+" ve "+sayi2+" sayılarının en büyük ortak böleni: "+ebob);
        }
 //
        Scanner kelimeAl = new Scanner(System.in);
        System.out.println("Kontrol etmek istediğiniz kelimeyi girin: ");
        String kelime = kelimeAl.nextLine();
        int altSinir = 0;
        int ustSinir = kelime.length()-1;
        boolean palindromeMu = true;

        while(altSinir < ustSinir){
            if(kelime.charAt(altSinir) != kelime.charAt(ustSinir)){
                palindromeMu = false;
                break;

            }
            altSinir++;
            ustSinir--;
        }
        if(palindromeMu){
            System.out.println(kelime+" kelimesi bir palindromdur.");
        }else{
            System.out.println(kelime+" kelimesi palindrom değildir.");
        }
        System.out.println(kelime.length());

 //
        Scanner sayilar = new Scanner(System.in);
        System.out.println("Üst sınırı giriniz: ");
        int girilenSayi = sayilar.nextInt();
        for(int i = 2 ; i <= girilenSayi ; i++){
            boolean asalMi = true;
            for(int j = 2;j<i;j++){
                if(i%j==0){
                    asalMi=false;
                    break;
                }
            }
            if(asalMi){
                System.out.print(i+", ");
            }
        }

        int cekilisSayisi = (int)(Math.random()*99 + 1);
        System.out.println("Tahmin sayınızı giriniz: ");
        int tahminSayisi;
        Scanner cekilis = new Scanner(System.in);
        tahminSayisi = cekilis.nextInt();
        if(tahminSayisi==cekilisSayisi){
            System.out.println("Sayıyı tamamen bildiniz ve 10.000 TL ödülü kazandınız!");
            System.out.println("Sizin tahmininiz: "+ tahminSayisi + " Şanslı sayı: "+cekilisSayisi);
        }else if(cekilisSayisi/10 == tahminSayisi % 10 && cekilisSayisi%10 == tahminSayisi/10){
            System.out.println("Sayının rakamlarını bildiniz ve 5.000 TL kazandınız!");
            System.out.println("Sizin tahmininiz: "+ tahminSayisi + " Şanslı sayı: "+ cekilisSayisi);
        }else if(cekilisSayisi/10 == tahminSayisi/10 || cekilisSayisi%10 == tahminSayisi/10 || cekilisSayisi/10 == tahminSayisi%10 || cekilisSayisi%10 == tahminSayisi%10){
            System.out.println("Sayının 1 rakamını bildiniz ve 1.000 TL ödül kazandınız!");
            System.out.println("Sizin tahmininiz: "+tahminSayisi+" Şanslı sayı: "+cekilisSayisi);
        }else{
            System.out.println("Şanslı Sayı: "+cekilisSayisi+ " Tekrar Deneyin!");




        }
*/









}
}

































