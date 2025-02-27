namespace Program;

class Program : Base
{
    public void Print() {
        Console.WriteLine("Print from Program!");
    }   
}


class MainClass : Program {

    public void Print() {
        Console.WriteLine("Print from derived!");
    }


    public static void Main() {
        new MainClass().Print();

        Program p = new MainClass();
        p.Print();

        Base b = new MainClass();
        b.Print();
    }

}

class Base {

    public virtual void Print() {
        Console.WriteLine("Print from base!");
    }   
}