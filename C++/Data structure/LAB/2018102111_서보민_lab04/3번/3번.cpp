#include "doublestack.h"
#include <iostream>
using namespace std;

int main() {
	doublestack doublestack1;
	for (int i = 1; i < 20; i++) {
		doublestack1.Push(i);
	}
	for (int i = 1001; i < 1020; i++) {
		doublestack1.Push(i);
	}
	doublestack1.Print();
}