// Header file for Queue ADT. 
#include <cstddef>
#include <iostream>
using namespace std;

class FullQueue
{};  

class EmptyQueue
{};  
 
template <class ItemType>
struct NodeType;

template <class ItemType>
class QueType
{
public: 
    QueType();
    QueType(int max);
    ~QueType();
    void MakeEmpty();
    bool IsEmpty() const;
    bool IsFull() const;
    void Enqueue(ItemType newItem);
    void Dequeue(ItemType& item);
private:
  NodeType<ItemType>* front;
  NodeType<ItemType>* rear;
};

template <class ItemType>
struct NodeType
{
  ItemType info;
  NodeType* next;
};


template <class ItemType>
QueType<ItemType>::QueType()          // Class constructor.
// Post:  front and rear are set to NULL.
{
  front = NULL;
  rear = NULL;
}

template <class ItemType>
void QueType<ItemType>::MakeEmpty()
// Post: Queue is empty; all elements have been deallocated.
{
  NodeType<ItemType>* tempPtr;

  while (front != NULL)
  {
    tempPtr = front;
    front = front->next;
    delete tempPtr;
  }
  rear = NULL;
}

template <class ItemType>          // Class destructor.
QueType<ItemType>::~QueType()
{
  MakeEmpty();
}

template<class ItemType>
bool QueType<ItemType>::IsFull() const
// Returns true if there is no room for another ItemType 
//  on the free store; false otherwise.
{
  NodeType<ItemType>* location;
  try
  {
    location = new NodeType<ItemType>;
    delete location;
    return false;
  }
  catch(bad_alloc exception)
  {
    return true;
  }
}

template <class ItemType>
bool QueType<ItemType>::IsEmpty() const
// Returns true if there are no elements on the queue; false otherwise.
{
  return (front == NULL);
}

template <class ItemType>
void QueType<ItemType>::Enqueue(ItemType newItem)
// Adds newItem to the rear of the queue.
// Pre:  Queue has been initialized.
// Post: If (queue is not full) newItem is at the rear of the queue;
//       otherwise a FullQueue exception is thrown.  

{
  if (IsFull())
    throw FullQueue();
  else
  {
    NodeType<ItemType>* newNode;

    newNode = new NodeType<ItemType>;
    newNode->info = newItem;
    newNode->next = NULL;
    if (rear == NULL)
      front = newNode;
    else
      rear->next = newNode;
    rear = newNode;
  }
}

template <class ItemType>
void QueType<ItemType>::Dequeue(ItemType& item)
// Removes front item from the queue and returns it in item.
// Pre:  Queue has been initialized and is not empty.
// Post: If (queue is not empty) the front of the queue has been 
//       removed and a copy returned in item; 
//       othersiwe a EmptyQueue exception has been thrown.
{
  if (IsEmpty())
    throw EmptyQueue();
  else
  {
    NodeType<ItemType>* tempPtr;

    tempPtr = front;
    item = front->info;
    front = front->next;
    if (front == NULL)
      rear = NULL;
    delete tempPtr;
  }
}

