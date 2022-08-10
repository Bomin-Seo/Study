#include <iostream>
using namespace std;

void main()
{
    int arr[10] = { 1, 3, 5, 17, 23, 45, 92, 120, 230, 493 };
    int num;
    cout << "input num : ";
    cin >> num;

    for (int i = 0; i < 10; i++)
    {
        if (arr[i] == num)
        {
            cout << "Find Index : " << i << endl;
            return;
        }
    }
    cout << "Not Found" << endl;
}