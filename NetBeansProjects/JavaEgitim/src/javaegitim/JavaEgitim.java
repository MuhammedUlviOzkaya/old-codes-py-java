/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaegitim;
import java.util.Scanner;
import jdk.nashorn.internal.ir.ContinueNode;

/**
 *
 * @author buzon
 */
public class JavaEgitim {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String user = "Buz";
        String password = "1433";
        int bakiye = 750;
        Scanner veri = new Scanner(System.in);
        int secim = -1;
        int i = 1;
        System.out.println("Hesap adını girin: ");
            String hesapAdi = veri.nextLine();
            System.out.println("Şifreyi girin: ");
            String hesapSifre = veri.nextLine();
            if(hesapAdi.equals(user)&&hesapSifre.equals(password)){
        
        while(i>0){
            
        if(i == 1){
            System.out.println("Hoşgeldiniz");
        }
        else{
            System.out.println(" ");
        }
            
                
            
                
                
                System.out.println("İşlem Seçiniz \n 1- Para Çekme \n 2- Para Yatırma \n 3- Bakiye Sorgulama \n Çıkmak için 0 tuşlayınız");
        secim = veri.nextInt();
        if(secim == 1){
            System.out.println("Mevcut Bakiye: "+bakiye+"\nÇekmek istediğiniz tutarı girin: ");
            int tutar = veri.nextInt();
            if(tutar <= bakiye){
                bakiye = bakiye-tutar;
                System.out.println("Çekilen Miktar: "+tutar +"\n Kalan Bakiye: "+bakiye);
            }
            else{
                System.out.println("Yetersiz Bakiye");
            }
            }
        if(secim == 2){
            System.out.println("Yatırılacak tutar: ");
            int yatirilan = veri.nextInt();
            bakiye = bakiye+yatirilan;
            System.out.println(yatirilan+" lira yatırıldı\n Yeni bakiye: "+bakiye);
        }
        if(secim==3){
            System.out.println("Mevcut Bakiye: "+bakiye);
        }
        else if(secim == 0){
            System.out.println("Çıkış yapıldı");
            break;
        }
        else{
            System.out.println("Geçersiz İşlem");
        }
        i++;
        
        }
            
        }
            else{
                System.out.println("Hata");
            }
        
        
        
      /*  
       smt.equals() yapısı ile string kontrol edilebilir.
        
        Scanner sayilar = new Scanner(System.in);
        int bakiye = 750;
        System.out.println("İşlem seçiniz \n1- Para Çekme \n2- Para Yatırma \n3- Bakiye Sorgulama\n Çıkmak için 0 tuşlayınız");
        int islem = sayilar.nextInt();
        switch(islem){
            case 1:
                System.out.println("Mevcut bakiye: "+bakiye+"\nÇekilecek tutarı girin: ");
                int tutar = sayilar.nextInt();
                bakiye = bakiye-tutar;
                System.out.println("Çekilen miktar: "+tutar+"\nYeni bakiye:"+bakiye);
                break;
            case 2:
                System.out.println("Mevcut bakiye:"+bakiye+"\nYatırılacak tutarı girin:");
                int yatirilacak = sayilar.nextInt();
                bakiye = bakiye + yatirilacak;
                System.out.println(yatirilacak+" lira yatırıldı\nYeni bakiye: "+bakiye);
                break;
            case 3:
                System.out.println("Bakiye: "+bakiye);
                break;
      */          
        
        
        
        
        
        }
        
        
      
      
      
      
      
    }
    

