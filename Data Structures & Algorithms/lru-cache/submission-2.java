class LRUCache {
    public class Node {
        public int key;
        public int val;
        public Node next;
        public Node prev;

        public Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    HashMap<Integer, Node> cache;
    int capacity;
    int size;
    Node startDummy;
    Node endDummy;
    public LRUCache(int capacity) {
        cache = new HashMap<>();

        startDummy = new Node(-1, -1);
        endDummy = new Node(-1, -1);
        startDummy.next = endDummy;
        endDummy.prev = startDummy;

        this.capacity = capacity;
        this.size = 0;
    }
    
    public int get(int key) {
        System.out.println("Getting for key: " + key);
        Node n = cache.get(key);
        if (n==null) return -1;
        remove(n);
        addToStart(n);
        return n.val;
    }
    
    public void put(int key, int value) {
        Node n = cache.get(key);
        if (n == null) {
            System.out.println("Creating new node: " + value + " at key: " + key);
            n = new Node(key, value);
            cache.put(key, n);
            addToStart(n);
        } else {
            n.val = value;
            System.out.println("Refreshing existing node: " + n.val + " at key: " + key);
            remove(n);
            addToStart(n);
        }

        if (size > capacity) {
            System.out.println("Evicting node: " + endDummy.prev.val);
            cache.remove(endDummy.prev.key);
            remove(endDummy.prev);
            System.out.println(cache.get(1));
        }
    }

    private void addToStart(Node n) {
        Node l1 = startDummy.next;
        startDummy.next = n;
        l1.prev = n;
        n.next = l1;
        n.prev = startDummy;
        size++;
    }

    private void remove(Node n) {
        Node next = n.next;
        Node prev = n.prev;

        if (next != null) next.prev = prev;
        if (prev != null) prev.next = next;
        n.next = null;
        n.prev = null;
        size--;
    }

}
