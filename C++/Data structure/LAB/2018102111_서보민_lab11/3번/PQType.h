// Definition of class PQType, which represents the Priority Queue ADT
class FullPQ{};
class EmptyPQ{};
#include "SortedType.h"
template<class ItemType>
class PQType
{
public:
  PQType();          // parameterized class constructor
  ~PQType();            // class destructor
  void MakeEmpty();
  bool IsEmpty() const;
  bool IsFull() const;
  void Enqueue(ItemType newItem);
  void Dequeue(ItemType& item);
private:
  int length;
  SortedType<ItemType> linkedlist;
  // int maxItems;
};

template<class ItemType>
PQType<ItemType>::PQType()
{
  length = 0;
}

template<class ItemType>
void PQType<ItemType>::MakeEmpty()
{
  length = 0;
}

template<class ItemType>
PQType<ItemType>::~PQType()
{
}
template<class ItemType>
void PQType<ItemType>::Dequeue(ItemType& item)
{
    if (length == 0)
        throw EmptyPQ();
    else {
        linkedlist.ResetList();
        linkedlist.GetNextItem(item);
        linkedlist.DeleteItem(item);
        length--;
    }
}


template<class ItemType>
void PQType<ItemType>::Enqueue(ItemType newItem)
{
    if (linkedlist.IsFull())
        throw FullPQ();
    else
    {
        length++;
        linkedlist.InsertItem(newItem); 
    }
}

template<class ItemType>
bool PQType<ItemType>::IsFull() const
// Post: Returns true if the queue is full; false, otherwise.
{
    return linkedlist.IsFull();
}

template<class ItemType>
bool PQType<ItemType>::IsEmpty() const
// Post: Returns true if the queue is empty; false, otherwise.
{
  return length == 0;
}

