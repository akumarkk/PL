namespace Volatile;

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


        worker.Stop();
        workerThread.Join();

        Console.WriteLine("worker is stopped");
    }
}

class Worker{

    private bool _stopWorker = false;

    public void DoWork(){
        while(!_stopWorker){
            // Console.Write("Working...");
            // Thread.Sleep(1000);
        }

        Console.Write("Working stopped...");
    }

    public void Stop(){
        _stopWorker = true;
    }

}