#include "UnsortedType.h"
#include <iostream>
using namespace std;

int main() {

	UnsortedType<int> unsort;
	unsort.InsertItem(2); unsort.InsertItem(6);
	unsort.InsertItem(7); unsort.InsertItem(4);
	unsort.InsertItem(9); unsort.InsertItem(5);

	unsort.Sort(unsort.get_listData());
	unsort.Print();
}