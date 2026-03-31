class MedianFinder {
    public PriorityQueue<Integer> small;
    public PriorityQueue<Integer> large;
    public MedianFinder() {
        //Maxheap
        small = new PriorityQueue<Integer>(Collections.reverseOrder());
        //Minheap
        large = new PriorityQueue<Integer>();
    }
    
    public void addNum(int num) {
        small.add(num);
        //Make sure every num small <= every num large
        if (!large.isEmpty() && small.peek() > large.peek()) {
            large.add(small.poll());
        }

        //Uneven size?
        if (small.size() > large.size() + 1) {
            large.add(small.poll());
        }
        if (large.size() > small.size() + 1) {
            small.add(large.poll());
        }
    }
    
    public double findMedian() {
        //Odd length?
        if (small.size() > large.size()) {
            return small.peek();
        }
        if (large.size() > small.size()) {
            return large.peek();
        }
        return (double) (small.peek() + large.peek()) / 2;
    }
}
