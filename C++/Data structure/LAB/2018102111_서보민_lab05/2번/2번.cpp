#include "QueType.h"
#include <iostream>
using namespace std;
void ReplaceItem(QueType&, int, int);

int main() {
	int item;
	QueType queue;
	QueType queue1;

	queue.Enqueue(2); queue.Enqueue(6); queue.Enqueue(7);
	queue.Enqueue(4); queue.Enqueue(5); queue.Enqueue(6);
	queue.Enqueue(10); queue.Enqueue(15); queue.Enqueue(6);

	queue1.Enqueue(2); queue1.Enqueue(6); queue1.Enqueue(7);
	queue1.Enqueue(4); queue1.Enqueue(5); queue1.Enqueue(6);
	queue1.Enqueue(10); queue1.Enqueue(15); queue1.Enqueue(6);

	cout << "a¹ø client function " << endl;
	ReplaceItem(queue, 6, 20);
	while (!queue.IsEmpty()) {
		queue.Dequeue(item);
		cout << item << " ";
	}
	cout << endl << endl;
	cout << "b¹ø Member function " << endl;
	queue1.ReplaceItem(6, 20);
	while (!queue1.IsEmpty()) {
		queue1.Dequeue(item);
		cout << item << " ";
	}
}

void ReplaceItem(QueType& queue, int oldItem, int newItem)
{
	int item;
	QueType temp_queue;
	while (!queue.IsEmpty()) {
		queue.Dequeue(item);
		if (item == oldItem)
			temp_queue.Enqueue(newItem);
		else {
			temp_queue.Enqueue(item);
		}
	}
	while (!temp_queue.IsEmpty()) {
		temp_queue.Dequeue(item);
		queue.Enqueue(item);
	}
}
