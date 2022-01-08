package oop_quiz;

public class Child extends Human implements Walkable, Runnable, Swimmable{
    public Child(String name, int age) {
        super(name, age, 5);
    }

    @Override
    public void swim(int x, int y) {
        printWhoAmI();
        System.out.println("swimming speed: " + (speed + 1));
        this.x = x;
        this.y = y;
        System.out.println("Swum to " + getLocation());
    }

    @Override
    public void run(int x, int y) {
        printWhoAmI();
        System.out.println("run speed: " + (speed + +2));
        this.x = x;
        this.y = y;
        System.out.println("Ran to " + getLocation());
    }

    @Override
    public void walk(int x, int y) {
        printWhoAmI();
        System.out.println("walk speed: " + speed);
        this.x = x;
        this.y = y;
        System.out.println("Walked to " + getLocation());
    }
}