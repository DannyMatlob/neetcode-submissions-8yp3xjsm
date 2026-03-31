class TimeMap {
    HashMap<String, List<Pair<Integer, String>>> keyStore;

    public TimeMap() {
        keyStore = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        keyStore.computeIfAbsent(key, k -> new ArrayList<>());

        keyStore.get(key).add(new Pair(timestamp, value));
    }
    
    public String get(String key, int timestamp) {
        String res = "";
        List<Pair<Integer, String>> list = keyStore.getOrDefault(key, new ArrayList<>());
        int l = 0;
        int r = list.size() - 1;

        while (l<=r) {
            int m = (l + r) / 2;
            if (list.get(m).key <= timestamp) {
                res = list.get(m).value;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return res;
    }

    private class Pair<K, V> {
        public K key;
        public V value;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }
}
