package SummerPackage;
import java.util.*;
import java.util.ArrayList;
public class PrimeDivisors {
    public static void main(String[] args) {
        ArrayList<String> smallestMultiple = new ArrayList<>();
        String template = "1^1";
        smallestMultiple.add(template);
        int limit = 10;
        for(int i = 1; i <= limit; i++){
            ArrayList<String> yeni = primeDivisors(i);


            for(int j = 0; j < yeni.size(); j++){
                int counter = 0;
                for(int k = 0; k < smallestMultiple.size(); k++){


                    if(smallestMultiple.get(k).charAt(0) == yeni.get(j).charAt(0)){
                        if(smallestMultiple.get(k).charAt(2) < yeni.get(j).charAt(2)){
                            smallestMultiple.set(k, yeni.get(j));
                        }
                    }



                    if(counter == smallestMultiple.size()){
                        smallestMultiple.add(yeni.get(j));
                    }

                }




            }
        }

        System.out.println(smallestMultiple);









    }





    public static ArrayList primeDivisors(int number){
        int controller = number;
        ArrayList<String> primes = new ArrayList<String>();
        for(int i = 2; i <= number / 2; i++){
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
        if(primes.size() == 0){
            String element = number + "^" + 1;
            primes.add(element);
        }
        return primes;
    }
}
