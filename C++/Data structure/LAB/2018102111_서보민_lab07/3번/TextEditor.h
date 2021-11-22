#include <iostream>
#include <string>
using namespace std;
typedef char ItemType;
struct LineType
{
	ItemType info[80];
    LineType* back;
    LineType* next;
};

class TextEditor
{
public:
    TextEditor();   
    ~TextEditor(); 
    void MakeEmpty();
    void InsertItem(ItemType* item);
    void GoToTop();
    void GoToBottom();
	void Print();
private:
	LineType* Header;
	LineType* Trailer;
    LineType* listData;
    LineType* currentLine;
};

TextEditor::TextEditor()
{
	Header = new LineType;
	Trailer = new LineType;
	strcpy_s(Header->info, "---Top of File---");
	strcpy_s(Trailer->info, "---Bottom of File---");
	Header->next = Trailer;
	Header->back = NULL;
	Trailer->back = Header;
	Trailer->next = NULL;
	listData = Header->next;
	currentLine = Header;
}
void TextEditor::GoToTop() {
	if (Header->next == Trailer) currentLine = Trailer;
	else {
		while (currentLine->back != NULL) currentLine = currentLine->back;
	}
}
void TextEditor::GoToBottom() {
	if (Trailer->back == Header) currentLine = Header; 
	else {
		while (Trailer->next != NULL) currentLine = currentLine->next;
	}
}
TextEditor::~TextEditor()
{
	MakeEmpty();
}
void TextEditor::MakeEmpty()
{
	LineType* tempPtr;
	while (listData != NULL)
	{
		tempPtr = listData;
		listData = listData->next;
		delete tempPtr;
	}
}
void TextEditor::InsertItem(ItemType* newline)
{
	LineType* newLine;
	newLine = new LineType;
	strcpy_s(newLine->info, newline);
	newLine->back = currentLine;
	newLine->next = currentLine->next;
	currentLine->next = newLine;
	currentLine = currentLine->next;
}
void TextEditor::Print() {
	GoToTop();
	while (currentLine != NULL) {
		cout << currentLine->info << endl;
		currentLine = currentLine->next;
	}
}