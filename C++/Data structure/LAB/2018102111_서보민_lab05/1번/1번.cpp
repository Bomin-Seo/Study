#include "QueType.h"
#include <iostream>
using namespace std;
#include <cstdlib>
#include <ctime>

int main() {
	QueType queue;
	srand((unsigned int)time(NULL));
	cout << "Enqueue items" << endl;
	for (int i = 0; i < 10; i++) {
		int item = rand();
		cout << item << endl;
		queue.Enqueue(item);
	}
	cout << endl;
	cout << "Dequeue items" << endl;
	for (int i = 0; i < 10; i++) {
		int item;
		queue.Dequeue(item);
		cout << item << endl;
	}
}