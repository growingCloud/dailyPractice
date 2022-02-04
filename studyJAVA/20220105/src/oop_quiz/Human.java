public class Human {
    String name;
    int age;
    int speed;
    int x, y;

    public Human(String name, int age, int speed, int x, int y) {
        this.name = name;
        this.age = age;
        this.speed = speed;
        this.x = x;
        this.y = y;
    }

    public Human(String name, int age, int speed) {
        this(name, age, speed, 0, 0);
    }

    public String getLocation() {
        return "(" + x + ", " + y + ")";
    }
    protected void printWhoAmI() {
        System.out.println("My name is " + name + ". " + age + " aged.");
    }
}