#include <iostream>
using namespace std;
#define MAX_ROWS 50
#define MAX_COLS 50

int NumPaths(int row, int col, int n)
{
	if ((row == n) || (col == n))
		return 1;
	else
		return NumPaths(row + 1, col, n) + NumPaths(row, col + 1, n);
}

int mat[MAX_ROWS][MAX_COLS];
int NumPaths_C(int row, int col, int n)
{
	if ((row == n) || (col == n))
		return 1;
	else {
		if (mat[row][col] == -1) {
			return NumPaths_C(row + 1, col, n) + NumPaths_C(row, col + 1, n);
		}
	}
	return mat[row][col];
}

int main() {
	for (int i = 0; i < 50; i++)
		for (int j = 0; j < 50; j++)
			mat[i][j] = -1;

	cout << NumPaths(2, 2, 3) << endl;
	cout << NumPaths_C(2, 2, 3) << endl;

	cout << NumPaths(5, 6, 15) << endl;
	cout << NumPaths_C(5, 6, 15) << endl;
}