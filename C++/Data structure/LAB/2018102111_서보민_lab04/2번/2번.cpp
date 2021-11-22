#include "StackTType.h"
#include <iostream>
using namespace std;

StackType<int> stackcopy(StackType<int> stack) {
	StackType<int> temp_stack;
	StackType<int> copy_stack;
	while (!stack.IsEmpty()) {
		int temp = stack.Top();
		temp_stack.Push(temp);
		stack.Pop();
	}
	while (!temp_stack.IsEmpty()) {
		int temp = temp_stack.Top();
		copy_stack.Push(temp);
		temp_stack.Pop();
	}
	return copy_stack;
}

int main() {
	StackType<int> stack, copy_stack;
	stack.Push(9);
	stack.Push(8);
	stack.Push(4);
	stack.Push(7);
	stack.Push(5);
	stack.Push(3);
	copy_stack = stackcopy(stack);
	cout << "Original Stack" << endl << endl;
	while (!stack.IsEmpty()) {
		int result = stack.Top(); // Return the recent value of stack!
		stack.Pop(); // Delete
		cout << result << endl;
	}
	cout << endl << "Copy Stack" << endl << endl;
	while (!copy_stack.IsEmpty()) {
		int result = copy_stack.Top(); // Return the recent value of stack!
		copy_stack.Pop(); // Delete
		cout << result << endl;
	}
}