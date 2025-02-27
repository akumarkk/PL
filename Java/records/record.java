// import person.Person;
class Main {
    public static void main(String[] args) {
        Person person = new Person("Aniket", 20);
        System.out.println(person);

        var person1 = new Person("Aniraj", 20);
        System.out.println(person1);

        var person2 = new Person("Aniraj", 20);
        System.out.println(person2);

        System.out.println("person1 == person = %b perons.equals(person1) = %b".formatted(person1 == person, person.equals(person1)));
        System.out.println("person1 == person2 = %b, person1.equals(person2) = %b".formatted(person1 == person2, person1.equals(person2)));
    }
}