#include "SortedType.h"
#include "UnsortedType.h"
#include <iostream>
using namespace std;

template <class ItemType>
void MergeLists(SortedType<ItemType>& l_a, SortedType<ItemType>& l_b, SortedType<ItemType>& result);
template <class ItemType>
void MergeLists(UnsortedType<ItemType>& l_a, UnsortedType<ItemType>& l_b, UnsortedType<ItemType>& result);

int main() {
	SortedType<int> sort1, sort2, result, result2;
	sort1.InsertItem(1); sort1.InsertItem(3);
	sort1.InsertItem(5); sort1.InsertItem(7);
	sort1.InsertItem(9); sort2.InsertItem(2);
	sort2.InsertItem(4); sort2.InsertItem(6);
	sort2.InsertItem(8); sort2.InsertItem(10);
	MergeLists(sort1, sort2, result);
	int item;
	cout << "A번 합병리스트" << endl;
	for (int i = 0; i < result.LengthIs(); i++) {
		result.GetNextItem(item);
		cout << item << ' ';
	}
	sort1.ResetList(); sort2.ResetList();
	cout << endl << endl;

	sort1.MergeLists(sort2, result2);
	cout << "B번 합병리스트" << endl;
	for (int i = 0; i < result2.LengthIs(); i++) {
		result2.GetNextItem(item);
		cout << item << ' ';
	}
	cout << endl << endl;
	// C, D번
	UnsortedType<int> unsort, unsort1, result3, result4;
	unsort.InsertItem(3); unsort.InsertItem(2);
	unsort.InsertItem(5); unsort.InsertItem(6);
	unsort.InsertItem(1); unsort1.InsertItem(7);
	unsort1.InsertItem(4); unsort1.InsertItem(9);
	unsort1.InsertItem(8); unsort1.InsertItem(10);
	cout << "C번 합병리스트" << endl;
	MergeLists(unsort, unsort1, result3);
	for (int i = 0; i < result3.LengthIs(); i++) {
		result3.GetNextItem(item);
		cout << item << ' ';
	}
	cout << endl << endl;
	unsort.ResetList(); unsort1.ResetList(); result3.ResetList();

	cout << "D번 합병리스트" << endl;
	unsort.MergeLists(unsort1, result4);
	for (int i = 0; i < result4.LengthIs(); i++) {
		result4.GetNextItem(item);
		cout << item << ' ';
	}
}

template <class ItemType>
void MergeLists(SortedType<ItemType>& l_a, SortedType<ItemType>& l_b, SortedType<ItemType>& result) {
	ItemType Item;
	for (int i = 0; i < l_a.LengthIs(); i++) {
		l_a.GetNextItem(Item);
		result.InsertItem(Item);
	}
	result.ResetList();
	for (int i = 0; i < l_b.LengthIs(); i++) {
		l_b.GetNextItem(Item);
		result.InsertItem(Item);
	}
}

template <class ItemType>
void MergeLists(UnsortedType<ItemType>& l_a, UnsortedType<ItemType>& l_b, UnsortedType<ItemType>& result) {
	ItemType Item;
	for (int i = 0; i < l_b.LengthIs(); i++) {
		l_b.GetNextItem(Item);
		result.InsertItem(Item);
	}
	for (int i = 0; i < l_a.LengthIs(); i++) {
		l_a.GetNextItem(Item);
		result.InsertItem(Item);
	}
}