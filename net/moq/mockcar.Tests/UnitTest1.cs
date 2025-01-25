namespace mockcar.Tests;

using Moq;

public class UnitTest
{
    [Fact]
    public void Test()
    {
        var mockCar = new Mock<Car.ICar>();
        mockCar.Setup(c => c.GetDetails()).Returns("id: 1, name: toyota");
        var details = mockCar.Object.GetDetails();

        Assert.Equal("id: 1, name: toyota", details);
    }
}