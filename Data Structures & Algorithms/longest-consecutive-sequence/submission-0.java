class Solution {
    public int longestConsecutive(int[] nums) {

        Map<Integer, Boolean> exploredMap = new HashMap<>();
        int longestLength = 0;

        for (int num : nums) {
            exploredMap.put(num, false);
        }

        for (int num : nums) {

            if (exploredMap.get(num)) continue;

            exploredMap.put(num, true);
            int currentLength = 1;

            int nextNum = num + 1;

            while (exploredMap.containsKey(nextNum) && !exploredMap.get(nextNum)) {
                exploredMap.put(nextNum, true);
                currentLength++;
                nextNum++;
            }

            int prevNum = num - 1;

            while (exploredMap.containsKey(prevNum) && !exploredMap.get(prevNum)) {
                exploredMap.put(prevNum, true);
                currentLength++;
                prevNum--;
            }

            longestLength = Math.max(longestLength, currentLength);
        }

        return longestLength;
    }
}