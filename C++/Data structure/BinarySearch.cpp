#include <iostream>
using namespace std;

/*
검색 대상이 배열 내에 존재한다면 index 반환
검색 대상이 배열 내에 존재하지 않는다면 -1을 반환한다.
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
찾고자 하는 값보다 작거나 같은 값 중에서 가장 큰 값을 반환한다.
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
찾고자 하는 값보다 크거나 같은 값들 중에서 가장 작은 값을 반환한다.
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