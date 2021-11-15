// Implementation file for Unsorted.h

#include "unsorted.h"
UnsortedType::UnsortedType()
{
  length = 0;
}
bool UnsortedType::IsFull() const
{
  return (length == MAX_ITEMS);
}

int UnsortedType::LengthIs() const
{
  return length;
}
void UnsortedType::RetrieveItem(ItemType& item, bool& found) 
// Pre:  Key member(s) of item is initialized. 
// Post: If found, item's key matches an element's key in the 
//       list and a copy of that element has been stored in item; 
//       otherwise, item is unchanged. 
{
  bool moreToSearch;
  int location = 0;
  found = false;

  moreToSearch = (location < length);

  while (moreToSearch && !found) 
  {
    switch (item.ComparedTo(info[location]))
    {
      case LESS    : 
      case GREATER : location++;
                     moreToSearch = (location < length);
                     break;
      case EQUAL   : found = true;
                     item = info[location];
                     break;
    }
  }
}
void UnsortedType::InsertItem(ItemType item)
// Post: item is in the list.
{
  info[length] = item;
  length++;
}
void UnsortedType::DeleteItem(ItemType item)
// Pre:  item's key has been initialized.
//       An element in the list has a key that matches item's.
// Post: No element in the list has a key that matches item's.
{
  int location = 0;

  while (item.ComparedTo(info[location]) != EQUAL)
    location++;

  info[location] = info[length - 1];
  length--;
}

void UnsortedType::DeleteItem_a(ItemType item){
//function     : 매개변수 item과 같은 요소가 있다면 요소를 삭제하며, 같은 요소가 없다면 변화가 일어나지 않는다.
//precondition : bool type 변수 deleted가 false로 초기화되어 있다.
//postcondition: 매개변수 item과 같은 요소가 있다면 해당 요소를 마지막 요소로 덧씌운 후, length를 1 감소시킨다.
//               요소 삭제 후, deleted의 값을 true로 바꾸어 for문의 루프에서 빠져나오며
//               같은 요소가 없다면 i == length가 되는 시점에서 검색을 멈춘다.
    bool deleted = false;
    for (int i = 0; i < length && !deleted; i++){
        if(item.CompareTo(info[i]) == EQUAL)
        {
            info[i] = info[length - 1];
            length--;
            deleted = true;
        } 
    }
}
void UnsortedType::DeleteItem_c(ItemType item) {
//function     : 매개변수 item과 동일한 요소가 list에 없다면 변경 작업을 시행하지 않고, 동일한 요소가 있다면 모든 동일한 요소를 삭제시킨다.
//precondition : 정수형 변수 i는 0으로 초기화한다.
//postcondition: 매개변수 item과 같은 요소 모두를 삭제하며 같은 요소가 없다면 변경 작업을 시행하지 않는다.
    int i = 0;
    while (i < length)
    {
        if (item.ComparedTo(info[i]) == EQUAL) {
            info[i] = info[length - 1];
            length--;
        }
        else {
            i++;
        }
    }
}
void UnsortedType::ResetList()
// Post: currentPos has been initialized.
{
  currentPos = -1;
}

void UnsortedType::GetNextItem(ItemType& item)
// Post: item is current item.
//       Current position has been updated.
{
  currentPos++;
  item = info[currentPos];
}
