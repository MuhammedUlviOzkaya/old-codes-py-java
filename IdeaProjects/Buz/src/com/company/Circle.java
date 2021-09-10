package com.company;

public class Circle {
    double radius;
    double area;
    double perimeter;

    public Circle(int radius){
        this.radius = radius;
    }

    public Circle(){
        this.radius = 3;
    }

    public double getCircleArea(){
        return Math.PI * radius * radius;
    }

    public double getCirclePerimeter(){
        return 2*Math.PI*radius;
    }



}
