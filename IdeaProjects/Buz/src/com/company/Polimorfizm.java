package com.company;

public class Polimorfizm {
    public static void main(String[] args){
        Canli canli = new Canli();
        canli.adiniSoyle();

        Canli kartal = new Kartal();
        kartal.adiniSoyle();
        ((Kartal)kartal).uc();

        Canli panda = new Panda();
        panda.adiniSoyle();
        ((Panda)panda).oyna();


    }

}

class Canli{

    public void adiniSoyle(){
        System.out.println("Ben bir canlı sınıfı nesnesiyim.");
    }

}

class Kartal extends Canli{

    @Override
    public void adiniSoyle() {
        System.out.println("Ben bir Kartal sınıfı nesnesiyim.");
    }

    public void uc(){
        System.out.println("Ben uçabilirim.");
    }

}

class Panda extends Canli{
    @Override
    public void adiniSoyle() {
        System.out.println("Ben bir panda sınıfı nesnesiyim.");
    }

    public void oyna(){
        System.out.println("Ben oyun oynamayı severim.");
    }
}
