class PrefixTree {
    class Node {
        public Node[] children = new Node[26];
        public boolean end = false;
    }

    private Node root = new Node();;

    public void insert(String word) {
        Node curr = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            int idx = 'z' - c;
            if (curr.children[idx] == null) curr.children[idx] = new Node();
            curr = curr.children[idx];
        }
        curr.end = true;
    }

    public boolean search(String word) {
        Node curr = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            int idx = 'z' - c;
            if (curr.children[idx] == null) return false;
            curr = curr.children[idx];
        }

        return curr.end;
    }

    public boolean startsWith(String prefix) {
        Node curr = root;
        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            int idx = 'z' - c;
            if (curr.children[idx] == null) return false;
            curr = curr.children[idx];
        }

        return true;
    }
}
