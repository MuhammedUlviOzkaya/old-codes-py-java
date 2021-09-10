package com.company;
import java.util.*;

public class ArraysCont {
    public static void main(String[] args){
        System.out.println(ebobBul(60,45));


    }
    public static int ekokBul(int birinciSayi, int ikinciSayi){
        int buyuk = Math.max(birinciSayi,ikinciSayi);
        int ekok=0;
        for(int i = buyuk; i<=birinciSayi*ikinciSayi; i++){
            if(i % birinciSayi == 0 && i % ikinciSayi == 0){
                ekok = i;
                break;
            }


        }
        return ekok;





    }
    public static int ebobBul(int birinciSayi, int ikinciSayi){
        int ebob = 1;
        int kontrol = 2;

        while(kontrol<=birinciSayi && kontrol <= ikinciSayi){
            if(birinciSayi % kontrol == 0 && ikinciSayi % kontrol == 0){
                ebob = kontrol;
            }
            kontrol++;

        }
        return ebob;



    }







}
