#include "SortedType.h"
#include <iostream>
using namespace std;

int main() {
	SortedType<char> s1;
	s1.InsertItem('X'); s1.InsertItem('Y');
	s1.InsertItem('Z');
	s1.PrintReverse();
}