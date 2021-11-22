#include <iostream>
using namespace std;
// #define MAX_ROWS 50
// #define MAX_COLS 50

/*
* SquareMatrix ADT Specification
* ---------------------------------------------------
* ���� : N x N (N <= 50 )�� ���簢 ���
* ---------------------------------------------------
* MakeEmpty(n)
* ��� : Matrix�� n�� �� ���θ� 0���� �ʱ�ȭ
* ���� : N�� �ִ� ũ��� 50
* ��� : N ���� �� ���� 0���� �ʱ�ȭ
* ---------------------------------------------------
* StoreValue(i, j, value)
* ��� : value��i��°��, j��° ���� ��ġ�� ����
* ���� : i,j�� �ִ� ���� 50
* ��� : ����� (i,j) ����� ������ value �� ����
* ---------------------------------------------------
* Add
* ��� : �� ����� �Բ� ���Ѵ�.
* ���� : ���� ũ���� �ٸ� ���簢 ���
* ��� : �� ����� ���� ���� ����
* ---------------------------------------------------
* Subtract
* ��� : �� ����� �ٸ� ������κ��� ����.
* ���� : ���� ũ���� �ٸ� ���簢 ���
* ��� : �� ����� ���� ���� ����
* ---------------------------------------------------
* Copy
* ��� : �� ����� �ٸ� ��ķ� �����Ѵ�.
* ���� : ���� ũ���� �ٸ� ���簢 ���
* ��� : ������ ��Ŀ� ���� ����� �� ����
* 
*/

const int MAX_ROWS = 50;
class SquareMatrix {
private:
	int matrix[50][50];
public:
	void MakeEmpty(int);
	void StoreValue(int, int, int);
	void Add(SquareMatrix);
	void Subtract(SquareMatrix);
	void Copy(SquareMatrix);
};
void SquareMatrix::MakeEmpty(int n) 
{ 
	int i, j = 0; 
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			matrix[i][j] = 0; 5s2f6r
}
void SquareMatrix::StoreValue(int i, int j, int value) 
{ 
	matrix[i][j] = value; 
}
void SquareMatrix::Add(SquareMatrix a) {
	SquareMatrix add_matrix;
	for (int i = 0; i < 50; i++) {
		for (int j = 0; j < 50; j++) {
			add_matrix.matrix[i][j] = matrix[i][j] + a.matrix[i][j];
		}
	}
}
void SquareMatrix::Subtract(SquareMatrix a) {
	SquareMatrix sub_matrix;
	for (int i = 0; i < 50; i++) {
		for (int j = 0; j < 50; j++) {
			sub_matrix.matrix[i][j] = matrix[i][j] - a.matrix[i][j];
		}
	}
}
void SquareMatrix::Copy(SquareMatrix a) {
	for (int i = 0; i < 50; i++) {
		for (int j = 0; j < 50; j++) {
			a.matrix[i][j] = matrix[i][j];
		}
	}
}