namespace PqTest;

using System.Diagnostics;
using MaxStack;


class PqTest {

    void Test() {
        PriorityQueue<Item, Item> pq = new(new ItemComparer());

        int cnt = 1;
        Item it = new Item() {Val = 1, Id = cnt++};
        pq.Enqueue(it, it);

        it = new Item() {Val = 5, Id = cnt++};
        pq.Enqueue(it, it);

        it = new Item() {Val = 2, Id = cnt++};
        pq.Enqueue(it, it);

        // Console.WriteLine(pq.Dequeue().Val);
        it = pq.Dequeue();
        Debug.Assert(it.Val == 5);
        Console.WriteLine(it.Val);
    
    }
}