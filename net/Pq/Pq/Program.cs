namespace Program;
using MaxStack;


public class Program {
    public static void Main(string[] args) {
        var obj = new MaxStack();
        obj.Push(5);
        obj.Push(1);
        obj.Push(5);


        var res = obj.PopMax();
        Console.WriteLine($"PopMax : {res}");

        var res2 = obj.Top();
        Console.WriteLine($"Top : {res2}");

        Console.WriteLine($"PeekMax : {obj.PeekMax()}");
        Console.WriteLine($"Pop : {obj.Pop()}");
        Console.WriteLine($"Pop : {obj.Top()}");
        
    }
    
}