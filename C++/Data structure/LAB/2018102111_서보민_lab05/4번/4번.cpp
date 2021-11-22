#include "QueType.h"
#include <iostream>
using namespace std;

int Length(QueType<int>&);
ItemType item;

int main() {
	
	QueType<int> queue;
	queue.Enqueue(7); queue.Enqueue(4); queue.Enqueue(5); 
	queue.Enqueue(6); queue.Enqueue(9);
	cout << "a¹ø Queue Length " << endl;
	cout << Length(queue) << endl;

	cout << "b¹ø Queue Length " << endl;
	cout << queue.Length() << endl;
}

int Length(QueType<int>& queue)
{
	int count = 0;
	QueType<int> temp_queue;

	while (!queue.IsEmpty()) {
		queue.Dequeue(item);
		count++;
		temp_queue.Enqueue(item);
	}
	while (!temp_queue.IsEmpty()) {
		temp_queue.Dequeue(item);
		queue.Enqueue(item);
	}
	return count;
}