class Solution {
    public int maxValue(int[][] e, int k) {
        Arrays.sort(e, (a, b) -> a[0] - b[0]); // 1. Sort the events by their start day (like organizing your calendar!) \U0001f4c5
        int n = e.length, dp[][] = new int[n + 1][k + 1]; // 2. Create a DP table to store our calculations. Think of it like a spreadsheet to keep track of the best fun levels for each combo. \U0001f4ca
        for (int i = n - 1; i >= 0; i--) { // 3. Loop through events *backwards* (from the end to the beginning), so we can build up our solution.  Going backwards lets us consider what happens if we *don't* attend the event. ⏪
            int l = i + 1, r = n, t = e[i][1], m, next = n; // 4. Binary search setup: l=left index, r=right index, t=end day of current event. We want to find the next non-overlapping event.
            while (l < r) // 5. Binary search loop to find the next event that doesn't overlap. Think of it like flipping through your schedule until you find an opening. \U0001f50d
                if (e[m = l + (r - l) / 2][0] > t) // 6. If the start day of the middle event is after our current event ends, it doesn't overlap. Move right boundary.
                    r = m;
                else // 7. Otherwise (it overlaps), shift the left boundary to exclude events that are overlapping.
                    l = m + 1;
            // l now points to the next non overlapping event
            for (int j = 0; j < k; j++) // 8. Loop through the allowed number of events we can attend. 
                dp[i][j] = Math.max(dp[i + 1][j], dp[l][j + 1] + e[i][2]); // 9.  This is the DP magic: Decide to either skip current event or pick the current event: Find the maximum value to the dp-table \U0001f31f.
                // dp[i+1][j]:  Don't attend event 'i'. What's the best we can do with same number of picks (j), from event 'i+1' onwards
                // dp[l][j+1] + e[i][2]: Attend event 'i'.  Add current event's value + use one 'pick' for current event, and look to the next compatible one (l)
        }
        return dp[0][0]; // 10. Return the maximum value from starting with the first event (0) and using zero events, this is the best possible outcome. \U0001f389
    }
}