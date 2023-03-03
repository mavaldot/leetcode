class Solution {
    public int[] shuffle(int[] nums, int n) {
        int l = nums.length; 
        int[] res = new int[l];
        int index = 0;
        
        for (int i = 0; i < n; i++) {
            res[index++] = nums[i];
            res[index++] = nums[n+i];
        }

        return res;
    }
}