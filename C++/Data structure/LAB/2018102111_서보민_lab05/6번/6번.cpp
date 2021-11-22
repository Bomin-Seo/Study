#include "QueType.h"
#include <iostream>
using namespace std;

int main() {
	QueType queue;
	ItemType item;
	queue.Enqueue(5); queue.Enqueue(4); queue.Enqueue(2);
	queue.Enqueue(3); queue.Enqueue(1); queue.Enqueue(8);
	while (!queue.IsEmpty()) {
		queue.MinDequeue(item);
		cout << item << " ";
	}
}