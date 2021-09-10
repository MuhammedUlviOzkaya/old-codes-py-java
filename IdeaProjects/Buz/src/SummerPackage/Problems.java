package SummerPackage;

public class Problems {
    public static void main(String[] args) {
        /*
        int sum = 0;

        for(int i = 0; i<1000; i++){
            if(i%3 == 0 || i%5 == 0){
                sum += i;
            }
        }
        System.out.println(sum);

        */



        Solve();


    }
    private static double SumDivisbleBy(int n, int p){
        return p/n + 1;
    }

    public static void Solve(){
        double result = 0;
        result = SumDivisbleBy(5,999);
        System.out.println(result);
    }
}
