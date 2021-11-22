#include "UnsortedType.h"
#include <iostream>
using namespace std;

int main() {
	// A¹ø
	UnsortedType<int> unsort;
	int item;
	unsort.InsertItem(1); unsort.InsertItem(6);
	unsort.InsertItem(5); unsort.InsertItem(2);
	unsort.InsertItem(3);
	
	unsort.DeleteItem(5);
	
	for (int i = 0; i < unsort.LengthIs(); i++) {
		unsort.GetNextItem(item);
		cout << item << ' ';
	}
	cout << endl;
	unsort.ResetList();
	unsort.DeleteItem(20);
	for (int i = 0; i < unsort.LengthIs(); i++) {
		unsort.GetNextItem(item);
		cout << item << ' ';
	}
	cout << endl << endl;
	// B¹ø
	UnsortedType<int> unsort1;
	unsort1.InsertItem(1); unsort1.InsertItem(6);
	unsort1.InsertItem(3); unsort1.InsertItem(6);
	unsort1.InsertItem(3);
	unsort1.DeleteItem(6);
	for (int i = 0; i < unsort1.LengthIs(); i++) {
		unsort1.GetNextItem(item);
		cout << item << ' ';
	}
}