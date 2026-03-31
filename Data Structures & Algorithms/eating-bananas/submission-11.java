class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int min = 1;
        int max = 0;
        int result = 0;
        for (int i : piles) {
            max = Math.max(max, i);
        }

        while (min <= max) {
            int mid = (max + min)/2;

            int hoursSpent = 0;
            for (int p : piles) {
                hoursSpent += Math.ceil((double) p / mid);
            }

            if (hoursSpent <= h) {
                result = mid;
                max = mid - 1;
            } else {
                min = mid + 1;
            }
        }

        return result;
    }
}
