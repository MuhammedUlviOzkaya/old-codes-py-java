
import java.util.*;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author buzon
 */
public class NewClass {
    public static void main(String[] args){
    
    // EXERCISE 3:    
  /*  Scanner sayilar = new Scanner(System.in);
    int num1,sum,average;
    int i = 1;
    sum = 0;
    while(sum<100){
        System.out.println("Enter a value: ");
        num1 = sayilar.nextInt();
        if(num1%10==0){
            System.out.println("Please enter another value: ");
        }else{
        sum = num1 + sum;
        System.out.println("Sum of the numbers is: "+sum); 
        System.out.println("Average of the numbers is: "+sum/i);
        i++;
        }
    */  
    Scanner second = new Scanner(System.in);
    System.out.println("Enter second: ");
    int seconds = second.nextInt();
    int x = 0;
    int y = 0;
    int a = minuteValue/60;
    int minuteValue = seconds/60-*60;
    int secondValue = seconds%60;
    int hourValue = minuteValue/60;
    while(x<1){
        System.out.print("The second value you entered equals = "+ hourValue +" hours,");
        x++;
    }
    for(y=0;y<1;y++){
        System.out.print(" "+ minuteValue + " minutes"); 
        y++;
    }
    System.out.println(" and "+ minuteValue%60+" seconds.");
    
        
        
        
        
    
    }
    
    
    
    
    
    
    
}
