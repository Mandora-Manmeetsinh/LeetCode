class Solution {
    public int minimumDeletions(String word, int k) {
        int[] freq = new int[26];

        for (char ch : word.toCharArray()) {
            freq[ch - 'a']++;
        }

        Arrays.sort(freq);

        int res = Integer.MAX_VALUE;
        int del = 0;

        for (int i=0; i<26; i++) {
            int minFreq = freq[i];
            int temp = del;

            for (int j=25; j> i; j--) {
                if (freq[j] - freq[i] <= k) {
                    break;
                }
                temp += freq[j] - minFreq - k;
            }

            res = Math.min(res , temp);
            del += minFreq;
        }
        return res;
    }
}