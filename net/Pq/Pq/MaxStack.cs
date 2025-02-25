namespace MaxStack;
public record Item {
    public int Val;
    public int Id;
}

public class ItemComparer: IComparer<Item> {
    public int Compare(Item i1, Item i2) {
        return i2.Val.CompareTo(i1.Val);
        // return i1.Id - i2.Id;
    }
}

public class MaxStack {
    PriorityQueue<Item, Item> pq = new(new ItemComparer());
    Stack<Item> st = new();
    int Id=0;
    

    public MaxStack() {
        
    }
    
    public void Push(int v) {
        var item = new Item() {Val = v, Id = this.Id++};
        st.Push(item);
        pq.Enqueue(item, item);
    }
    
    public int Pop() {
        Item it = st.Pop();
        // Item res;
        // int p;
        pq.Remove(it, out var res, out var p);
        return it.Val;
    }
    
    public int Top() {
        Item it = st.Peek();
        return it.Val;
        
    }
    
    public int PeekMax() {
        Item it = pq.Peek();
        return it.Val;
    }
    
    public int PopMax() {
        Item it = st.Pop();
        pq.Dequeue();

        return it.Val;
        
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.PeekMax();
 * int param_5 = obj.PopMax();
 */