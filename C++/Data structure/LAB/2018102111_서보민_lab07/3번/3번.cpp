#include "TextEditor.h"
#include <iostream>

using namespace std;

int main() {
	TextEditor text;
	ItemType line1[80] = "This is the first line of text";
	ItemType line2[80] = "This is the current line of text";
	ItemType line3[80] = "This is the last line of text";
	text.InsertItem(line1);
	text.InsertItem(line2);
	text.InsertItem(line3);
	
	text.Print();
}