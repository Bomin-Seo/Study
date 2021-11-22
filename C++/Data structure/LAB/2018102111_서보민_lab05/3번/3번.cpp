#include "QueType.h"
#include <iostream>
using namespace std;
bool Identical(QueType<int>&, QueType<int>&);

int main() {
	bool result;
	QueType<int> queue, queue1;
	queue.Enqueue(2); queue.Enqueue(6); queue.Enqueue(7);
	queue.Enqueue(4); queue.Enqueue(5); queue.Enqueue(6);
	queue.Enqueue(10); queue.Enqueue(15); queue.Enqueue(3);

	queue1.Enqueue(2); queue1.Enqueue(6); queue1.Enqueue(7);
	queue1.Enqueue(4); queue1.Enqueue(5); queue1.Enqueue(6);
	queue1.Enqueue(12); queue1.Enqueue(15); queue1.Enqueue(3);

	cout << "a¹ø client function " << endl;
	result = Identical(queue, queue1);
	if (result == 0) cout << "False" << endl;
	else cout << "True" << endl;

	// Queue reset
	queue.Enqueue(2); queue.Enqueue(6); queue.Enqueue(7);
	queue.Enqueue(4); queue.Enqueue(5); queue.Enqueue(6);
	queue.Enqueue(10); queue.Enqueue(15); queue.Enqueue(3);

	queue1.Enqueue(2); queue1.Enqueue(6); queue1.Enqueue(7);
	queue1.Enqueue(4); queue1.Enqueue(5); queue1.Enqueue(6);
	queue1.Enqueue(12); queue1.Enqueue(15); queue1.Enqueue(3);

	cout << "b¹ø Member function " << endl;
	result = queue.Identical(queue1);
	if (result == 0) cout << "False" << endl;
	else cout << "True" << endl;
	
}

bool Identical(QueType<int>& queue, QueType<int>& queue1)
{
	int item, item1;
	while (!queue.IsEmpty() && !queue1.IsEmpty()) {
		queue.Dequeue(item);
		queue1.Dequeue(item1);
		if (item != item1) {
			return false;
		}
	}
	return true;
}