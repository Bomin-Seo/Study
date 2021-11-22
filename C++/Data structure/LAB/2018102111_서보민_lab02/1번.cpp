#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream input_file(argv[1]);
	ofstream output_file(argv[2]);
	
	char ch;
	while (!input_file.eof())
	{
		input_file.get(ch);
		if (input_file.fail()) break;
		if (ch == '\r')
			output_file << "\n";
		else
			output_file << ch;
	}
	input_file.close();
	output_file.close(); 
	return 0;
}