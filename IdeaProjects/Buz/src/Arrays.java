import java.util.Scanner;

public class Arrays {
    public static void main(String[] args) {
     /*   System.out.println("Kaç sayının ortalaması alınacak?");
        double ortalama = 0;
        Scanner veri = new Scanner(System.in);
        int eleman = veri.nextInt();
        int sayiOrtalamasi[] = new int[eleman];
        for(int i = 0;i<eleman;i++){
            System.out.println((i+1)+". sayıyı girin: \n");
            sayiOrtalamasi[i] = veri.nextInt();
            ortalama = ortalama + sayiOrtalamasi[i];
        }
        System.out.println("Girilen sayıların ortalaması: "+(ortalama/eleman));

    swapValues();






    }
    public static void swapValues(){
        int sayilar [] = new int[10];
        Scanner veri = new Scanner(System.in);
        int evenCounter = 0;
        int oddCounter = 0;


        for(int i = 0;i<sayilar.length;i++){
            System.out.println("Enter the "+(i+1)+ ". number: ");
            sayilar[i] = veri.nextInt();

        }
        System.out.println("Number of even numbers: "+ evenCounter+"\nNumber of odd numbers: "+oddCounter);








        int [] copy = new int[buz.length];
        for(int j = 0; j<copy.length; j++){
            System.out.println("Copy dizisinin "+(j+1)+". elemanı: "+copy[j]);
        }
        for(int i = 0; i<buz.length; i++){
            copy[i] = buz[i];
        }
        for(int j = 0; j<copy.length; j++){
            System.out.println("Copy dizisinin "+(j+1)+". elemanı: "+copy[j]);
        }
 */
        int [][] numbers = {{1,2,3},{4,5,6},{7,8,9}};
        int counter = 0;
        for(int line = 0; line< numbers.length; line++){
            for(int column = 0; column< numbers[line].length; column++){
                System.out.println(line+"X"+column+": "+numbers[line][column]);
                counter++;
            }
        if(counter%3==0)
            System.out.println("");



        }





    }
    public static void reverseArray(int [] array){
        int [] reverse = new int[array.length];
        for(int i = 0, j = array.length-1; i<array.length ; i++, j--){
            reverse[i] = array[j];

            System.out.println("Reverse dizisinin "+(i+1)+". elemanı : "+reverse[i]);
        }





    }
    public static void findSumss(int ... arrays){
            int toplam = 0;
        for(int c : arrays){
            toplam += c;
        }
        System.out.println("Girilen değerlerin toplamı= "+toplam);


    }
    public static void diziGoster(int dizi[]){
        for(int i : dizi){
            System.out.println(i);
        }


    }
    public static void diziYazdir(String dizi[]){
        for(String a : dizi)
            System.out.println(a);


    }





}
