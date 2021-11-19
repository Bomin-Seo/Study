#include <iostream>
#include "TreeType.h"
#include "SortedType.h"

void AddElement(TreeType& tree, int Array[], int from, int to);
void MakeTree(TreeType& tree, SortedType<int>& list);
void MakeTree(TreeType& tree, SortedType<int>& list)
{
	int length = list.LengthIs();
	int* array = new int[length];
	int item_info;
	int i;
	list.ResetList();
	for (i = 0; i < length; i++)
	{
		list.GetNextItem(item_info);
		array[i] = item_info;
	}
	AddElement(tree, array, 0, length - 1);
	delete[] array;
}
void AddElement(TreeType& tree, int Array[], int front, int rear)
{
	int mid;
	if (front <= rear) {
		mid = (front + rear)/2;
		tree.InsertItem(Array[mid]);
		AddElement(tree, Array, front, mid - 1);
		AddElement(tree, Array, mid + 1, rear);
	}
}