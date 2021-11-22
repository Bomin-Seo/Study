#include <iostream>
using namespace std;

class FullStack
{};

class EmptyStack
{};

const int MAX_ITEMS = 200;

class doublestack {
private: 
	int top_small;
	int top_big;
	int items[MAX_ITEMS];
public:
	doublestack();
	bool IsFull() const;
	void Push(int item);
	void Print();
};

doublestack::doublestack() {
	top_small = 0;
	top_big = MAX_ITEMS - 1;
}

bool doublestack::IsFull() const
{
	bool result = (top_small + 1) == top_big;
	return result;
}

void doublestack::Push(int item)
{
	if (IsFull()) {
		throw FullStack();
	}
	else {
		if (item <= 1000) {
			items[top_small] = item;
			top_small++;
		}
		else {
			items[top_big] = item;
			top_big--;
		}
	}
}

void doublestack::Print()
{
	while (top_small > 0) {
		top_small--;
		cout << items[top_small] << endl;
	}

	while (top_big < MAX_ITEMS - 1) {
		top_big++;
		cout << items[top_big] << endl;
	}
}


