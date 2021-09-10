package SummerPackage;

public class FibonacciEven {
    public static void main(String[] args) {
        double a = 600851475143.0;
        int n = 2;

        while ( n * n < a)
        {
            while(a % n == 0)
            {
                a = a / n;

            }
            n ++;
        }

        System.out.println(a);



    }
}
