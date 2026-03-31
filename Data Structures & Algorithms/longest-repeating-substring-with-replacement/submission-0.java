class Solution {
    public int characterReplacement(String s, int k) {
        int res = 0;
        int[] counts = new int[26];
        int biggestCount = 0;
        int l = 0;
        int r = 0;
        for (r = 0; r < s.length(); r++) {
            counts[s.charAt(r) - 'A']++;
            biggestCount = Math.max(biggestCount, counts[s.charAt(r) - 'A']);
            
            //While the length of the window minus the biggest count is greater than the replacements we have available
            while ((r - l + 1) - biggestCount > k) {
                counts[s.charAt(l) - 'A']--;
                l++;
            }
            res = Math.max(res, r-l+1);
        }
        return res;
    }
}
