class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;

        // Map: Old Node -> New Node
        HashMap<Node, Node> map = new HashMap<>();

        // Pass 1: Create all new nodes (don't wire them yet)
        Node curr = head;
        while (curr != null) {
            map.put(curr, new Node(curr.val));
            curr = curr.next;
        }

        // Pass 2: Wire next and random pointers
        curr = head;
        while (curr != null) {
            // map.get(curr) is the copy we made
            map.get(curr).next = map.get(curr.next);
            map.get(curr).random = map.get(curr.random);
            curr = curr.next;
        }

        return map.get(head);
    }
}