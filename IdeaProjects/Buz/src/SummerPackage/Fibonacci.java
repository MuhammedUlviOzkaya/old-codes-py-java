package SummerPackage;

public class Fibonacci {
    public static void main(String [] args){

        long a = 0;
        long b = 1;
        long c = 1;

        int sum = 0;

        do {
            a = b;
            b = c;
            c = a + b;

            if(c%2 == 0){
                sum += c;
            }
        }
        while(c < 4000000) ;

        System.out.println(sum);












    }

}
