#include "PQType.h"
#include <iostream>

using namespace std;
/*
예측
					56
			28				42
		26		27		40		19
	25	   24  5  15   2  3

x = 56 
y = 42
z = 40

출력값
56 42 40
*/
int main() {
	PQType<int> pq(50);

	pq.Enqueue(56);
	pq.Enqueue(27);
	pq.Enqueue(42);
	pq.Enqueue(26);
	pq.Enqueue(15);
	pq.Enqueue(3);
	pq.Enqueue(19);
	pq.Enqueue(25);
	pq.Enqueue(24);
	pq.Enqueue(5);

	int x, y, z;
	pq.Enqueue(28);
	pq.Enqueue(2);
	pq.Enqueue(40);
	pq.Dequeue(x);
	pq.Dequeue(y);
	pq.Dequeue(z);

	cout << x << " " << y << " " << z << endl;
}