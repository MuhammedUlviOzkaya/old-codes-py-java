package com.company;
import java.util.Scanner;

public class ExercisePage {
    int x;
    int modelYear;
    String modelName;

    public ExercisePage(int year, String name){
        modelYear = year;
        modelName = name;

    }
    public static void main(String [] args){
        ExercisePage object = new ExercisePage(2019,"Mercedes");
        System.out.println(object.modelYear+" "+object.modelName);








   /*

        String kartTurleri[] = {"Kupa","Maça","Sinek","Karo"};
        String kartNumaralari[] = {"As","2","3","4","5","6","7","8","9","10","J","Q","K"};
        int deste[] = new int[52];

        desteyiOlustur(deste);

        desteyiGoster(deste,kartTurleri,kartNumaralari);



    }

    private static void desteyiKaristir(int[] deste) {
        for(int i = 0; i<deste.length; i++){
            int randomIndex = (int)(Math.random()*52);

            int gecici = deste[randomIndex];
            deste[i] = deste[randomIndex];
            deste[randomIndex] = gecici;

        }

    }

    private static void desteyiOlustur(int[] deste) {
        for(int i = 0; i<deste.length; i++){
            deste[i] = i;

        }
    }

    private static void desteyiGoster(int[] deste, String[] kartTurleri, String[] kartNumaralari) {
        for(int i = 0; i<deste.length; i++){
            String kartTuru = kartTurleri[deste[i]/13];
            String kartNumarasi = kartNumaralari[deste[i]%13];
            System.out.println(kartTuru +" "+kartNumarasi);


        }
*/

    }

}
