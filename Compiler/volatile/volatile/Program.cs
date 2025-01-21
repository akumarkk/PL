namespace Volatile;


// dotnet run -c Release
internal class Program
{
    static void Main(string[] args)
    {

        Worker worker = new Worker();
        Thread workerThread = new Thread(worker.DoWork);
        workerThread.Start();
        while(!workerThread.IsAlive){
            // Thread.Sleep(1000);

        }
        Console.WriteLine("worker is alive");

        Thread.Sleep(500);
        worker.Stop();
        workerThread.Join();

        Console.WriteLine("worker is stopped");
    }
}

class Worker{

    private bool _stopWorker = false;

    public void DoWork(){
        bool work = false;
        while(!_stopWorker){
            // Console.Write("Working...");
            // Thread.Sleep(500);
            work = !work;
        }

        Console.Write("Working stopped...");
    }

    public void Stop(){
        _stopWorker = true;
    }

}