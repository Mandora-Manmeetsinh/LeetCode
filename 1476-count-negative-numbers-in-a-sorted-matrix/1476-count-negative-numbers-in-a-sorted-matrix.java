class Solution {
    public int countNegatives(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int nag = 0;

        for (int i=0; i<row; i++) {
            for (int j=0; j<col; j++) {
                if (grid[i][j] < 0) {
                    nag++;
                }
            }
        }
        return nag;
    }
}