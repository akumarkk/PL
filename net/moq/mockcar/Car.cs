namespace Car;


public class Car
{
    public int Id { get; set; }
    public string? Name { get; set; }

    public Car(int id, string? name)
    {
        Id = id;
        Name = name;
    }

    public virtual string GetDetails()
    {
        return $"id: {Id}, name: {Name}";
    }
}

public interface ICar
{
    string GetDetails();
}