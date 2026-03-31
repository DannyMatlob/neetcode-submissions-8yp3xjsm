class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Deque<int[]> stack = new ArrayDeque<>();
        int[] result = new int[temperatures.length];

        stack.push(new int[]{temperatures[0], 0});
        for (int i = 1; i<temperatures.length; i++) {
            System.out.println(stack);
            while (!stack.isEmpty() && temperatures[i] > stack.peekLast()[0]) {
                int[] item = stack.pollLast();
                result[item[1]] = i - item[1];
            }
            stack.addLast(new int[]{temperatures[i], i});
        }
        return result;
    }
}
