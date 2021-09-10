package SummerPackage;

public class TriangularNumber {
    public static void main(String [] args){

        int i = 1;
        while(divisorCounter(triangularNumber(i)) < 501){
            i++;
        }
        System.out.println(triangularNumber(i));


    }
    public static long triangularNumber(long number){
        return number * (number + 1) / 2;

    }
    public static long divisorCounter(long number){
        if(number == 1){
            return 1;
        }
        long controller = number;
        int divisors = 1;
        int isDivisible = 0;
        for(int i = 2; i * i <= number; i++){
            int counter = 0;
            while(controller % i == 0){
                controller /= i;
                counter += 1;
                isDivisible += 1;
            }
            divisors *= (counter + 1);
        }
        if(isDivisible == 0){
            return 2;
        }
        return divisors;

    }
}
