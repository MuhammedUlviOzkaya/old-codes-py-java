package StartInterface;

import java.util.ArrayList;

public class CokluKalitimGerekliligi {
    public static void main(String[] args) {
        MuslumBaba muslum = new MuslumBaba();
        muslum.sahnedeDansEt();
        muslum.sahnedeSigaraIc();


        PopSarkiciOzellikleri popSarkici1 = new Tarkan();
        PopSarkiciOzellikleri popSarkici2 = new Beyonce();

        PopSarkiciOzellikleri dizi[] = new PopSarkiciOzellikleri[5];
        dizi[0] = popSarkici1;
        dizi[1] = popSarkici2;

        ArrayList<PopSarkiciOzellikleri> sarkicilar = new ArrayList<>();
        sarkicilar.add(popSarkici1);
        sarkicilar.add(popSarkici2);




    }
}




interface Kisi{
    void yemekYe();
    void sporYap();
}

interface UniversiteOgrencisi{
    void gezToz();
}

interface OgrenciOzellikleri extends Kisi, UniversiteOgrencisi{
    void dersCalis();
    void okulaGit();
    void sisteminKopegiOl();
}

class Student implements OgrenciOzellikleri {

    @Override
    public void gezToz() {

    }

    @Override
    public void yemekYe() {

    }

    @Override
    public void sporYap() {

    }

    @Override
    public void dersCalis() {

    }

    @Override
    public void okulaGit() {

    }

    @Override
    public void sisteminKopegiOl() {

    }
}

interface ArabeskSarkiciOzellikleri {
    void sahnedeSigaraIc();
}

interface PopSarkiciOzellikleri {
    void sahnedeDansEt();
}

class Tarkan implements PopSarkiciOzellikleri{

    @Override
    public void sahnedeDansEt() {

    }
}

class Beyonce implements PopSarkiciOzellikleri{
    @Override
    public void sahnedeDansEt() {

    }
}

class MuslumBaba implements ArabeskSarkiciOzellikleri, PopSarkiciOzellikleri {


    @Override
    public void sahnedeSigaraIc() {

    }

    @Override
    public void sahnedeDansEt() {

    }
}


