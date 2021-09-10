package SummerPackage;

import java.util.ArrayList;

public class SmallestMultiple {
    public static void main(String[] args) {
        int number = 10;
        int controller = number;
        ArrayList<String> primes = new ArrayList<String>();
        for(int i = 2; i <= number; i++){
            int counter = 0;
            while(controller % i == 0){
                controller /= i;
                counter++;
            }
            if(counter != 0){
                String element = i + "^" + counter + " ";
                primes.add(element);
            }
        }


        for(int i = 1; i <= number; i++){

        }




    }
}
