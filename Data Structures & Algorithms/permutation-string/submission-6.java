class Solution {
    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character, Integer> initialMap = mapFromString(s1);

        for (int i = 0; i < s2.length() - s1.length() + 1; i++) {
            var subMap = mapFromString(s2.substring(i, i+s1.length()));
            System.out.println(subMap);
            if (initialMap.equals(subMap)) {
                return true;
            }
        }
        return false;
    }

    public HashMap<Character, Integer> mapFromString(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        return map;
    }
}
