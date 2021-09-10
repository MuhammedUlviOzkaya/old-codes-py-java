package newJavaPackage;

public class MyCalculator {
    public static void main(String[] args){

        Daire daire1 = new Daire(4);
        System.out.println(daire1.cevreHesapla());
        System.out.println(daire1.alanHesapla());

    }

}

class Daire{
    private int yariCap;
    public final double PI = 3.14;
    public double alan;
    public double cevre;

    public Daire(int yaricap){
        this.yariCap = yaricap;
    }

    public double cevreHesapla(){

        cevre = 2*PI*yariCap;
        return cevre;
    }

    public double alanHesapla(){

        alan = PI*Math.pow(yariCap,2);
        return alan;
    }

}












