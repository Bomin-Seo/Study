#include <iostream>
using namespace std;
// #define MAX_ROWS 50
// #define MAX_COLS 50

/*
* SquareMatrix ADT Specification
* ---------------------------------------------------
* 구조 : N x N (N <= 50 )의 정사각 행렬
* ---------------------------------------------------
* MakeEmpty(n)
* 기능 : Matrix의 n행 열 내부를 0으로 초기화
* 조건 : N의 최대 크기는 50
* 결과 : N 안의 행 열은 0으로 초기화
* ---------------------------------------------------
* StoreValue(i, j, value)
* 기능 : value를i번째행, j번째 열의 위치에 저장
* 조건 : i,j의 최대 값은 50
* 결과 : 행렬의 (i,j) 요소의 값으로 value 값 저장
* ---------------------------------------------------
* Add
* 기능 : 두 행렬을 함께 더한다.
* 조건 : 같은 크기의 다른 정사각 행렬
* 결과 : 두 행렬을 합의 값을 도출
* ---------------------------------------------------
* Subtract
* 기능 : 한 행렬을 다른 행렬으로부터 뺀다.
* 조건 : 같은 크기의 다른 정사각 행렬
* 결과 : 두 행렬의 차의 값을 도출
* ---------------------------------------------------
* Copy
* 기능 : 한 행렬을 다른 행렬로 복사한다.
* 조건 : 같은 크기의 다른 정사각 행렬
* 결과 : 지정한 행렬에 기존 행렬의 값 복사
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