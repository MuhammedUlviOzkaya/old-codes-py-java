package com.company;

public class Immutable {
    public static void main(String[] args){
    BuzOne exa = new BuzOne(2019,"Porsche");
        System.out.println("Our car is "+exa.modelYear+" model "+exa.modelName);






    }
}

class BuzOne{
    int modelYear;
    String modelName;

    public BuzOne(int number,String model){
        modelYear = number;
        modelName = model;

    }

    public BuzOne(){
        modelYear = 2000;
        modelName = "Merco";
    }
    public void speed(int maxSpeed){

        System.out.println("Max speed is: "+maxSpeed);
    }
}








