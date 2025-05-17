class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int rows = mat.length, cols = mat[0].length;
        List<Integer> res = new ArrayList<>();

        for (int d = 0; d < (rows + cols - 1); d++) {
            List<Integer> diag = new ArrayList<>();

            int row = (d < cols) ? 0 : (d - cols) + 1;
            int col = (d < cols) ? d : cols - 1;

            while (row < rows && col >= 0) {
                diag.add(mat[row++][col--]);
            }

            if (d % 2 == 0) Collections.reverse(diag);

            res.addAll(diag);
        }

        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}