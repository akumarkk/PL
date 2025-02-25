namespace OrderedDict;
using System.Collections.Specialized;
class Program
{
    static void Main(string[] args)
    {
        OrderedDictionary dict = new();
        dict.Add("a", 1);
        dict.Add("b", 2);
        dict.Add("c", 3);
        dict.Add("d", 4);
        dict.Add("e", 5);
        dict.Add("f", 6);
        dict.Add("g", 7);
        dict.Add("h", 8);
        dict.Add("i", 9);
        dict.Add("j", 10);
        // dict.Add("a", 1);
        dict["a"] = 10;


        for(int i=0; i<dict.Count; i++) {
            Console.WriteLine(dict[i]);
        }

        Console.WriteLine(dict[1]);
    }
}