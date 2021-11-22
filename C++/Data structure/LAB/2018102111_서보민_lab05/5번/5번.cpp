#include "QueType.h"
#include <iostream>
using namespace std;

int main() {
	QueType<int> queue(6);
	ItemType item;
	queue.Enqueue(1); queue.Enqueue(2); queue.Enqueue(3);
	queue.Enqueue(4); queue.Enqueue(5); queue.Enqueue(6); queue.Enqueue(7);
	cout << queue.LengthIs() << endl;
	queue.Dequeue(item); queue.Dequeue(item);
	cout << queue.LengthIs() << endl;
}