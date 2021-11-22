#include "StackType.h"
#include <iostream>
using namespace std;

int main() {
	StackType stack1, stack2;
	stack1.Push(2); stack1.Push(4);
	stack1.Push(6); stack1.Push(8);
	cout << "stack1에 요소 추가 및 stack2 copy" << endl;
	stack1.Print();
	cout << endl;

	stack2.Copy(stack1);
	
	stack1.Push(1); stack1.Push(3);
	cout << "copy후 stack1에 요소 추가" << endl;
	stack1.Print();
	cout << endl;
	cout << "stack2 요소 출력" << endl;
	while (!stack2.IsEmpty()) {
		int Item = stack2.Top();
		stack2.Pop();
		cout << Item << " ";
	}
	cout << endl;
	cout << "stack1의 주소 :" << &stack1 << endl;
	cout << "stack2의 주소 :" << &stack2 << endl;

}