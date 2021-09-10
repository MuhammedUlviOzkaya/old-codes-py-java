package com.company;
        import java.util.Scanner;

public class StaticKavrami {
    public static void main(String[] args) {
        int[][] a = new int[][] { { 1, 2, 3},{ 4, 5, 6},{ 7, 8, 9} };
        int[][] b = new int[][] { { 13, 14, 15},{ 10, 11, 12},{ 16, 17, 18} };
        int[][] c = new int[3][3];

        if(a.length == b.length && a[0].length == b[0].length){
            for(int i = 0; i<a.length; i++){

                for(int j = 0; j<a[i].length; j++){
                    c[i][j] = a[i][j] + b[i][j];
                }
            }
        }
        else{
            System.out.println("The length of the arrays are different.");
        }

        for(int i = 0; i<c.length; i++){
            for(int j = 0; j<c[i].length; j++){
                System.out.print(c[i][j]+" ");
            }
        }











    }

    public static void arraySecondLargest(){
        int dizi [] = {12,354,65,34,1123,434,54565,434,234};
        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;
        for(int i = 0; i<dizi.length; i++){
            if(dizi[i]>largest){
                largest = dizi[i];
            }
            for(int j = 0; j<dizi.length; j++){
                if(secondLargest<dizi[j] && dizi[j]<largest){
                    secondLargest = dizi[j];
                }
            }
        }


        System.out.println("Largest is: "+largest+"\nSecond largest is: "+secondLargest);
    }

    public static void crFullPrmd(int satirSayisi) {
        int s = satirSayisi - 1;
        for (int i = 1; i <= satirSayisi; i++) {
            for (int j = 0; j < s; j++) {
                System.out.print(" ");
            }
            s = s - 1;
            for (int j = 0; j < (2 * i - 1); j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void crPrmd2(int satirSayisi) {
        for (int i = 0; i < satirSayisi; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void crPrmd1(int satirSayisi) {
        int i, j, k;
        k = (satirSayisi - 1) * 2;
        for (i = 0; i < satirSayisi; i++) {
            for (j = 0; j < k; j++) {
                System.out.print(" ");
            }
            k = k - 2;
            for (j = 0; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public static boolean isPolindrome(String word) {
        String control = word.toLowerCase();
        boolean polindrome = false;
        int max = control.length() - 1;
        int min = 0;
        for (int i = 0; i < control.length() / 2; i++) {
            if (control.charAt(min) == control.charAt(max)) {
                polindrome = true;

            } else {
                polindrome = false;
            }
            min++;
            max--;
        }
        return polindrome;
    }

    public static void numPolindrome(int num) {

        int no = num;
        int rev = 0;

        while(num>0){
            int basamak = num%10;
            rev = basamak + 10*rev;
            num = num/10;



        }
        if(no==rev){
            System.out.println("Girdiğiniz sayı polindromdur.");
        }else{
            System.out.println("Girdiğiniz sayı polindrom değildir.");
        }



    }

    public static int countWord(String s){
        int word = 1;
        for(int i = 0; i<s.length()-1; i++){
            if(s.charAt(i)==' ' && s.charAt(i+1) != ' '){
                word++;
            }
        }
        return word;
    }

    public static int kelimeSay(String s){
        int word = 1;
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i) == ' ' && s.charAt(i+1) != ' '){
                word++;
            }
        }
        return word;
    }
}





