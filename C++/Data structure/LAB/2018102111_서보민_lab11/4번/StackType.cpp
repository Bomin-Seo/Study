
#include <cstddef>
#include <new>
#include "StackType.h"
/*
A.최우선 원소는 가장 큰 timeStamp를 가진 원소입니다.

C. 4장의 Push는 O(1)이며, PQ로 구현된 Push도 node를 만들고,
   이전에 Push된 원소의 timestamp보다 1 큰 값을 입력한 후로 push하므로 O(1)입니다.
   4장의 Pop은 O(1)이며, PQ로 구현된 Pop은 timestamp가 정렬되지 않은 경우
   처음부터 끝까지 원소를 탐색해봐야 하므로 O(N)입니다.
*/
void StackType::Push(ItemType newItem)
{
  if (IsFull())
    throw FullStack();
  else
  {
    NodeType* location;
    location = new NodeType;
    location->info = newItem;
    location->next = topPtr;
    if (topPtr == NULL) location->timestamp = 0;
    else location->timestamp = topPtr->timestamp + 1;
    topPtr = location;
  }
}
void StackType::Pop()
{
  if (IsEmpty())
    throw EmptyStack();
  else
  {  
    NodeType* tempPtr;
    tempPtr = topPtr;
    NodeType* HighPriority = topPtr;
    while (tempPtr != NULL) {
        if (tempPtr->timestamp > HighPriority->timestamp) {
            HighPriority = tempPtr;
        }
        tempPtr = tempPtr->next;
    }
    topPtr = topPtr->next;
    delete HighPriority;
  }
}
ItemType StackType::Top()
{
  if (IsEmpty())
    throw EmptyStack();
  else
    return topPtr->info;  
}
bool StackType::IsEmpty() const
{
    return (topPtr == NULL);
}
bool StackType::IsFull() const
{
  NodeType* location;
  try
  {
    location = new NodeType;
    delete location;
    return false;
  }
  catch(std::bad_alloc)
  {
    return true;
  }
}

StackType::~StackType()
{
    NodeType* tempPtr;

    while (topPtr != NULL)
    {
        tempPtr = topPtr;
        topPtr = topPtr->next;
        delete tempPtr;
    }
}

StackType::StackType()
{
    topPtr = NULL;
}

