#include "SortedType.h"
#include <iostream>
using namespace std;

int main() {
	// A번
	SortedType<int> sort;
	int item;
	sort.InsertItem(1); sort.InsertItem(2);
	sort.InsertItem(3); sort.InsertItem(4);
	sort.InsertItem(5);
	cout << "A번 Sorted List" << endl;
	for (int i = 0; i < sort.LengthIs(); i++) {
		sort.GetNextItem(item);
		cout << item << ' ';
	}
	cout << endl;
	sort.ResetList();
	sort.DeleteItem_a(2);
	cout << "A번 Sorted List 존재요소 제거" << endl;
	for (int i = 0; i < sort.LengthIs(); i++) {
		sort.GetNextItem(item);
		cout << item << ' ';
	}
	cout << endl;
	sort.ResetList();
	sort.DeleteItem_a(20);
	cout << "A번 Sorted List 존재하지 않는요소 제거" << endl;
	for (int i = 0; i < sort.LengthIs(); i++) {
		sort.GetNextItem(item);
		cout << item << ' ';
	}
	cout << endl << endl;
	//B번
	SortedType<int> sort2;
	sort2.InsertItem(1); sort2.InsertItem(2);
	sort2.InsertItem(2); sort2.InsertItem(4);
	sort2.InsertItem(5);
	cout << "B번 Sorted List" << endl;
	for (int i = 0; i < sort2.LengthIs(); i++) {
		sort2.GetNextItem(item);
		cout << item << ' ';
	}
	cout << endl;
	sort2.ResetList();
	sort2.DeleteItem_b(2);
	cout << "B번 Sorted List 존재요소 제거" << endl;
	for (int i = 0; i < sort2.LengthIs(); i++) {
		sort2.GetNextItem(item);
		cout << item << ' ';
	}
	cout << endl;
	sort2.ResetList();
	sort2.DeleteItem_b(20);
	cout << "B번 Sorted List 존재하지 않는요소 제거" << endl;
	for (int i = 0; i < sort2.LengthIs(); i++) {
		sort2.GetNextItem(item);
		cout << item << ' ';
	}
}