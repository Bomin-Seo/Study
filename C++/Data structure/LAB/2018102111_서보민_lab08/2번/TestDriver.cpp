#include <iostream>
using namespace std;

/*
재귀버전이 더 비효율적이라고 생각합니다.
재귀 버전에서 수열의 n번째 요소를 구하기 위해서는 n-1, n-2를 매개변수로 가지는
2개의 함수를 호출해야하며 n-1, n-2이 0 또는 1이 될 때까지 같은 과정을 반복하여 함수를 호출하여야합니다.
하지만 비 재귀버전을 배열을 통하여 구현한다면, 앞의 두 요소를 더하여 n번째 요소를 구하기 때문에
동작이 상당히 줄어들기 때문에 비 재귀버전이 더 효율적이라고 생각합니다.
*/

int Fibonacci_recursive(int n);
int Fibonacci_non_recursive(int n);

int main() {
	cout << Fibonacci_recursive(10) << endl;
	cout << Fibonacci_non_recursive(10) << endl;
	return 0;

}

int Fibonacci_recursive(int n) {
	if (n == 1 || n == 0) 
		return n; 
	return Fibonacci_recursive(n - 1) + Fibonacci_recursive(n - 2);
}

int Fibonacci_non_recursive(int n) {
	int *fibo = new int[n + 1];
	fibo[0] = 0;
	fibo[1] = 1;
	for (int i = 2; i < n + 1; i++) {
		fibo[i] = fibo[i - 2] + fibo[i - 1];
	}
	return fibo[n];
	delete[] fibo;
}