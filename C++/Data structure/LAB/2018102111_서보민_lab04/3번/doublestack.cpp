#include "doublestack.h"
#include <iostream>

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
	while (top_small != 0) {
		cout << items[top_small] << endl;
		top_small;
	}

	while (top_big < MAX_ITEMS - 1) {
		cout << items[top_big] << endl;;
		top_big++;
	}
}