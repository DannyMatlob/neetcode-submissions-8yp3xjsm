class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] pairs = new int[position.length][2];
        for (int i = 0; i < position.length; i++) {
            pairs[i][0] = position[i];
            pairs[i][1] = speed[i];
        }
        Arrays.sort(pairs, (a,b) -> Integer.compare(b[0], a[0]));
        
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        for (int[] cur : pairs) {
            if (timeToFinish(cur, target) > timeToFinish(stack.peekLast(), target)) {
                System.out.println("Pushing pair: {" + cur[0] + ", " + cur[1] + "}");
                stack.addLast(cur);
            }
        }

        return stack.size();
    }

    private double timeToFinish(int[] pair, int target) {
        if (pair==null) return 0;
        return ((double) target - pair[0]) / pair[1];
    }
}
