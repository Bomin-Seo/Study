#include "QueType.h"

QueType<int>::QueType(int max)
// Parameterized class constructor
// Post: maxQue, front, and rear have been initialized.
//       The array to hold the queue elements has been dynamically
//       allocated.
{
    maxQue = max + 1;
    front = maxQue - 1;
    rear = maxQue - 1;
    items = new ItemType[maxQue];
}
QueType<int>::QueType()          // Default class constructor
// Post: maxQue, front, and rear have been initialized.
//       The array to hold the queue elements has been dynamically
//       allocated.
{
    maxQue = 501;
    front = maxQue - 1;
    rear = maxQue - 1;
    items = new ItemType[maxQue];
}
QueType<int>::~QueType<int>()         // Class destructor
{
    delete[] items;
}

void QueType<int>::MakeEmpty()
// Post: front and rear have been reset to the empty state.
{
    front = maxQue - 1;
    rear = maxQue - 1;
}

bool QueType<int>::IsEmpty() const
// Returns true if the queue is empty; false otherwise.
{
    return (rear == front);
}

bool QueType<int>::IsFull() const
// Returns true if the queue is full; false otherwise.
{
    return ((rear + 1) % maxQue == front);
}

void QueType<int>::Enqueue(ItemType newItem)
// Post: If (queue is not full) newItem is at the rear of the queue;
//       otherwise a FullQueue exception is thrown.  
{
    if (IsFull())
        throw FullQueue();
    else
    {
        rear = (rear + 1) % maxQue;
        items[rear] = newItem;
    }
}

void QueType<int>::Dequeue(ItemType& item)
// Post: If (queue is not empty) the front of the queue has been 
//       removed and a copy returned in item; 
//       othersiwe a EmptyQueue exception has been thrown.
{
    if (IsEmpty())
        throw EmptyQueue();
    else
    {
        front = (front + 1) % maxQue;
        item = items[front];
    }
}
int QueType<int>::Length()
{
    if (front <= rear)
        return rear - front;
    else {
        return rear + maxQue - front;
    }
}