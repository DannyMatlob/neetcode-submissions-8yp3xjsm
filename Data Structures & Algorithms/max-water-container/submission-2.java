class Solution {
    public int maxArea(int[] heights) {
        int p1 = 0;
        int p2 = heights.length-1;
        int max = 0;
        while (p2>p1) {
            int curArea = Math.min(heights[p1], heights[p2]) * Math.abs(p2 - p1);
            max = Math.max(max, curArea);
            if (heights[p1] < heights[p2]) {
                p1++;
            } else {
                p2--;
            }
        }
        return max;
    }
}
