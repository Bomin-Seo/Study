#include <iostream>
using namespace std;

/*
�˻� ����� �迭 ���� �����Ѵٸ� index ��ȯ
�˻� ����� �迭 ���� �������� �ʴ´ٸ� -1�� ��ȯ�Ѵ�.
*/
int BinarySearch_a(int array[], int sizeOfArray, int value) {
    int midPoint;
    int first = 0;
    int last = (sizeOfArray - 1);
    bool moreToSearch = (first <= last);
    bool found = false;
    int Pos = -1;
    while (moreToSearch && !found) {
        midPoint = (first + last) / 2;
        if (array[midPoint] > value) {
            last = midPoint - 1;
            moreToSearch = (first <= last);
        }
        else if (array[midPoint] < value) {
            first = midPoint + 1;
            moreToSearch = (first <= last);
        }
        else {
            found = true;
            Pos = midPoint;
            break;
        }
    }
    if (!found)
        Pos = -1;
    return Pos;
}

/*
ã���� �ϴ� ������ �۰ų� ���� �� �߿��� ���� ū ���� ��ȯ�Ѵ�.
*/
int BinarySearch_b(int array[], int sizeOfArray, int value) {
    int midPoint;
    int first = 0;
    int last = (sizeOfArray - 1);
    bool moreToSearch = (first <= last);
    bool found = false;
    int Pos = -1;
    while (moreToSearch && !found) {
        midPoint = (first + last) / 2;
        if (array[midPoint] > value) {
            last = midPoint - 1;
            moreToSearch = (first <= last);
        }
        else if (array[midPoint] < value) {
            first = midPoint + 1;
            moreToSearch = (first <= last);
        }
        else {
            found = true;
            Pos = midPoint;
            break;
        }
    }
    if (!found)
        Pos = last;
    return array[Pos];
}

/*
ã���� �ϴ� ������ ũ�ų� ���� ���� �߿��� ���� ���� ���� ��ȯ�Ѵ�.
*/
int BinarySearch_c(int array[], int sizeOfArray, int value) {
    int midPoint;
    int first = 0;
    int last = (sizeOfArray - 1);
    bool moreToSearch = (first <= last);
    bool found = false;
    int Pos = -1;
    while (moreToSearch && !found) {
        midPoint = (first + last) / 2;
        if (array[midPoint] > value) {
            last = midPoint - 1;
            moreToSearch = (first <= last);
        }
        else if (array[midPoint] < value) {
            first = midPoint + 1;
            moreToSearch = (first <= last);
        }
        else {
            found = true;
            Pos = midPoint;
            break;
        }
    }
    if (!found)
        Pos = first;

    return array[Pos];
}

int main()
{
    int arr[10] = { 1, 3, 5, 17, 23, 45, 92, 120, 230, 493 };
    int result, result2, result3, result4;
    result = BinarySearch_a(arr, 10, 23);
    result2 = BinarySearch_a(arr, 10, 6);
    result3 = BinarySearch_b(arr, 10, 22);
    result4 = BinarySearch_c(arr, 10, 46);
    cout << result << " " << result2 << " " << result3 << " " << result4;
}