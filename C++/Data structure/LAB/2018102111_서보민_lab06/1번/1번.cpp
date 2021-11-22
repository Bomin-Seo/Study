#include "StackType.h"
#include <iostream>
using namespace std;

void ReplaceItem(StackType& stack, ItemType oldItem, ItemType newItem);

int main() {
	// A번 문제
	StackType stack;
	StackType stack1;
	stack.Push(1); stack.Push(2);
	stack.Push(3); stack.Push(2);

	stack1.Push(1); stack1.Push(2);
	stack1.Push(3); stack1.Push(2);
	cout << "A번 문제 Replace 전 stack" << endl;
	while (!stack.IsEmpty()) {
		ItemType item = stack.Top();
		cout << item << " ";
		stack.Pop();
	}
	cout << endl;
	ReplaceItem(stack1, 2, 6);
	cout << "A번 문제 Replace 후 stack" << endl;
	while (!stack1.IsEmpty()) {
		ItemType item1 = stack1.Top();
		cout << item1 << " ";
		stack1.Pop();
	}
	cout << endl << endl;
	// B번 문제
	stack.Push(1); stack.Push(2);
	stack.Push(3); stack.Push(2);

	stack1.Push(1); stack1.Push(2);
	stack1.Push(3); stack1.Push(2);
	cout << "B번 문제 Replace 전 stack" << endl;
	while (!stack.IsEmpty()) {
		ItemType item = stack.Top();
		cout << item << " ";
		stack.Pop();
	}
	cout << endl;
	stack1.ReplaceItem(2, 6);
	cout << "B번 문제 Replace 후 stack" << endl;
	while (!stack1.IsEmpty()) {
		ItemType item1 = stack1.Top();
		cout << item1 << " ";
		stack1.Pop();
	}
}
void ReplaceItem(StackType& stack, ItemType oldItem, ItemType newItem)
{
	StackType temp_stack;
	ItemType temp_item;
	while (!stack.IsEmpty()) {
		temp_item = stack.Top();
		if (temp_item == oldItem) temp_stack.Push(newItem);
		else temp_stack.Push(temp_item);
		stack.Pop();
	}
	while (!temp_stack.IsEmpty()) {
		temp_item = temp_stack.Top();
		stack.Push(temp_item);
		temp_stack.Pop();
	}
}