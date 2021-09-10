
package javaapplicationbuz;

import java.util.Scanner;


public class JavaApplicationBuz {

    
    public static void main(String[] args) {
        
        createDifferentPyramid(4);
        createPyramid(4);
        
        
        
        
        
        
        
        
        
        
    }
    public static void createPyramid(int sayi){
        for(int i = 0; i<sayi; i++){
            for(int j = 0; j<=i; j++){
                System.out.print("* ");
            }
            System.out.println("");
        }
    }
    
    public static void createDifferentPyramid(int sayi){
        int i,j,k;
        k = (sayi-1)*2;
        for(i = 0; i<sayi; i++){
            for(j=0; j<k; j++){
                System.out.print(" ");
            }
            k = k-2;
            for(j=0; j<=i; j++){
                System.out.print("* ");
            }
            System.out.println("");
        }
        
        
        
    }
   
    
    
    }
     
    
    

