#include "QueType.h"
#include <iostream>
using namespace std;

template <class ItemType>
void ReplaceItem(QueType<ItemType>& queue, ItemType oldItem, ItemType newItem);

int main() {
	QueType<int> queue;
	QueType<int> queue1;
	int item;
	queue.Enqueue(1); queue.Enqueue(3);
	queue.Enqueue(2); queue.Enqueue(3);
	queue1.Enqueue(1); queue1.Enqueue(3);
	queue1.Enqueue(2); queue1.Enqueue(3);
	cout << "A번 Replace 전 queue" << endl;

	while (!queue.IsEmpty()) {
		queue.Dequeue(item);
		cout << item << " ";
	}
	cout << endl;
	ReplaceItem(queue1, 3, 5);
	cout << "A번 Replace 후 queue" << endl;

	while (!queue1.IsEmpty()) {
		queue1.Dequeue(item);
		cout << item << " ";
	}
	cout << endl << endl;

	queue.Enqueue(1); queue.Enqueue(3);
	queue.Enqueue(2); queue.Enqueue(3);
	queue1.Enqueue(1); queue1.Enqueue(3);
	queue1.Enqueue(2); queue1.Enqueue(3);
	cout << "B번 Replace 전 queue" << endl;
	while (!queue.IsEmpty()) {
		queue.Dequeue(item);
		cout << item << " ";
	}
	cout << endl;

	queue1.ReplaceItem(3, 5);
	cout << "B번 Replace 후 queue" << endl;
	
	while (!queue1.IsEmpty()) {
		queue1.Dequeue(item);
		cout << item << " ";
	}
}

template <class ItemType>
void ReplaceItem(QueType<ItemType>& queue, ItemType oldItem, ItemType newItem)
{
	QueType<ItemType> temp_queue;
	ItemType item;
	while (!queue.IsEmpty()) {
		queue.Dequeue(item);
		if (item == oldItem) temp_queue.Enqueue(newItem);
		else temp_queue.Enqueue(item);
	}
	while (!temp_queue.IsEmpty()) {
		temp_queue.Dequeue(item);
		queue.Enqueue(item);
	}
}