#include "QueType.h"

QueType::QueType(int max)
// Parameterized class constructor
// Post: maxQue, front, and rear have been initialized.
//       The array to hold the queue elements has been dynamically
//       allocated.
{
    maxQue = max + 1;
    front = maxQue - 1;
    rear = maxQue - 1;
    items = new ItemType[maxQue];
    Length = 0;
    minimum_pos = -1;
}
QueType::QueType()          // Default class constructor
// Post: maxQue, front, and rear have been initialized.
//       The array to hold the queue elements has been dynamically
//       allocated.
{
    maxQue = 501;
    front = maxQue - 1;
    rear = maxQue - 1;
    items = new ItemType[maxQue];
    Length = 0;
    minimum_pos = -1;
}
QueType::~QueType()         // Class destructor
{
    delete[] items;
}

void QueType::MakeEmpty()
// Post: front and rear have been reset to the empty state.
{
    front = maxQue - 1;
    rear = maxQue - 1;
    Length = 0;
    minimum_pos = -1;
}

bool QueType::IsEmpty() const
// Returns true if the queue is empty; false otherwise.
{
    return (Length == 0);
}

bool QueType::IsFull() const
// Returns true if the queue is full; false otherwise.
{
    return (Length == maxQue);
}

void QueType::Enqueue(ItemType newItem)
// Post: If (queue is not full) newItem is at the rear of the queue;
//       otherwise a FullQueue exception is thrown.  
{
    if (IsFull())
        throw FullQueue();
    else
    {
        for (int i = 0; i < Length; i++) {
            if (items[i] == -1) {
                items[i] = newItem;
                break;
            }
        }
        rear = (rear + 1) % maxQue;
        items[rear] = newItem;
        Length++;
    }
}

void QueType::Dequeue(ItemType& item)
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
        Length--;
    }
}
int QueType::LengthIs()
{
    return Length;
}

void QueType::MinDequeue(ItemType& item) {
    if (IsEmpty())
        throw EmptyQueue();
    else
    {
        front = (front + 1) % maxQue;
        int pos;
        if (front <= rear) {            
            int min_value = 10000;
            for (pos = 0; pos <= rear; pos++) {
                if (items[pos] == -1) {
                    continue;
                }
                if (items[pos] < min_value) {
                    min_value = items[pos];
                    minimum_pos = pos;
                }
            }
            item = items[minimum_pos];
            items[minimum_pos] = -1;
            Length--;
        }
        else {
            int min_value = 10000;
            for (pos = 0; pos <= rear; pos++) {
                if (items[pos] == -1) {
                    continue;
                }
                if (items[pos] < min_value) {
                    min_value = items[pos];
                    minimum_pos = pos;
                }
            }
            for (pos = front; front <= maxQue; pos++) {
                if (items[pos] == -1) {
                    continue;
                }
                if (items[pos] < min_value) {
                    min_value = items[pos];
                    minimum_pos = pos;
                }
            }
            item = items[minimum_pos];
            items[minimum_pos] = -1;
            Length--;
        }
    }
}
