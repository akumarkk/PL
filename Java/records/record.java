// import person.Person;



class Main {
private class EqualObj {
    int val;
    String name;

    public EqualObj(int val, String name) {
        this.val = val;
        this.name = name;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof EqualObj) {
            EqualObj another = (EqualObj) obj;
            return val == another.val && name.equals(another.name);
        }
        return false;
    }
}

public EqualObj getEqualObj() {
    return new EqualObj(10, "Aniket");
}

    public static void main(String[] args) {
        Person person = new Person("Aniket", 20);
        System.out.println(person);

        var person1 = new Person("Aniraj", 20);
        System.out.println(person1);

        var person2 = new Person("Aniraj", 20);
        System.out.println(person2);

        System.out.println("person1 == person = %b perons.equals(person1) = %b".formatted(person1 == person, person.equals(person1)));
        System.out.println("person1 == person2 = %b, person1.equals(person2) = %b".formatted(person1 == person2, person1.equals(person2)));
    
        Main main = new Main();
        EqualObj equal = main.getEqualObj();
        EqualObj equal1 = main.getEqualObj();
        System.out.println(equal == equal1);

        System.out.println(equal.equals(equal1));
    }
}