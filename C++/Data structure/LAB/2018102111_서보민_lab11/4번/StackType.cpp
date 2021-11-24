
#include <cstddef>
#include <new>
#include "StackType.h"
/*
A.�ֿ켱 ���Ҵ� ���� ū timeStamp�� ���� �����Դϴ�.

C. 4���� Push�� O(1)�̸�, PQ�� ������ Push�� node�� �����,
   ������ Push�� ������ timestamp���� 1 ū ���� �Է��� �ķ� push�ϹǷ� O(1)�Դϴ�.
   4���� Pop�� O(1)�̸�, PQ�� ������ Pop�� timestamp�� ���ĵ��� ���� ���
   ó������ ������ ���Ҹ� Ž���غ��� �ϹǷ� O(N)�Դϴ�.
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

