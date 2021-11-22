#include <iostream>
using namespace std;

template <class ItemType>
struct NodeType;

template <class ItemType>
class UnsortedType
{
public:
  UnsortedType();   
  ~UnsortedType();  
  bool IsFull() const;
  int  LengthIs() const;
  void MakeEmpty();
  void RetrieveItem(ItemType& item, bool& found);
  void InsertItem(ItemType item); 
  void DeleteItem(ItemType item);
  void ResetList();
  void GetNextItem(ItemType& item);
  void Sort(NodeType<ItemType>* location);
  NodeType<ItemType>* get_listData();   
  void Print();
private:
  NodeType<ItemType>* listData;
  int length;
  NodeType<ItemType>* currentPos;
  NodeType<ItemType>* MinLoc(NodeType<ItemType>* location, NodeType<ItemType>* minPtr);
};

template<class ItemType>
struct NodeType
{
    ItemType info;
    NodeType* next;
};

template <class ItemType>
UnsortedType<ItemType>::UnsortedType()  // Class constructor
{
  length = 0;
  listData = NULL;
}

template <class ItemType>
UnsortedType<ItemType>::~UnsortedType()
{
  MakeEmpty();
}  
template<class ItemType>
bool UnsortedType<ItemType>::IsFull() const
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
int UnsortedType<ItemType>::LengthIs() const
{
  return length;
}
template <class ItemType>
void UnsortedType<ItemType>::MakeEmpty()
{
    NodeType<ItemType>* tempPtr;

    while (listData != NULL)
    {
        tempPtr = listData;
        listData = listData->next;
        delete tempPtr;
    }
    length = 0;
}
template <class ItemType>
void UnsortedType<ItemType>::RetrieveItem(ItemType& item, 
    bool& found)
{
    bool moreToSearch;
    NodeType<ItemType>* location;

    location = listData;
    found = false;
    moreToSearch = (location != NULL);

    while (moreToSearch && !found)
    {
        if (item == location->info)
        {
            found = true;
            item = location->info;
        }
        else
        {
            location = location->next;
            moreToSearch = (location != NULL);
        }
    }
}
template <class ItemType>
void UnsortedType<ItemType>::InsertItem(ItemType item)
{
    NodeType<ItemType>* location;

    location = new NodeType<ItemType>;
    location->info = item;
    location->next = listData;
    listData = location;
    length++;
}
template <class ItemType>
void UnsortedType<ItemType>::DeleteItem(ItemType item)
{
    NodeType<ItemType>* location = listData;
    NodeType<ItemType>* tempLocation;

    // Locate node to be deleted.
    if (item == listData->info)
    {
        tempLocation = location;
        listData = listData->next;		// Delete first node.
    }
    else
    {
        while (!(item==(location->next)->info))
            location = location->next;

        // Delete node at location->next
        tempLocation = location->next;
        location->next = (location->next)->next;
    }
    delete tempLocation;
    length--;
}

template <class ItemType>
void UnsortedType<ItemType>::ResetList()
{
  currentPos = NULL;
}
 
template <class ItemType>
void UnsortedType<ItemType>::GetNextItem(ItemType& item)
{
  if (currentPos == NULL)
    currentPos = listData;
  else
    currentPos = currentPos->next;
  item = currentPos->info;
} 

template <class ItemType>
NodeType<ItemType>* UnsortedType<ItemType>::MinLoc(NodeType<ItemType>* location, NodeType<ItemType>* minPtr)
{
    if (location != NULL)
    {
        if (location->info < minPtr->info)
            minPtr = location;
        if (location->next == NULL)
            return minPtr;
        return MinLoc(location->next, minPtr);
    }
    else
        return minPtr;
}

template <class ItemType>
void UnsortedType<ItemType>::Sort(NodeType<ItemType>* location)
// location->next == NULL인 성립되는 상황에서 먼저 location과 minPtr의 info값을 비교하여
// minPtr이 가장 작은 info를 가지는 node를 지칭하도록 한 뒤, 바로 minPtr을 return하여 함수의 초기 호출되었을
// 때 까지 돌아오는 동작을 줄여 효율적으로 동작시킬 수 있다고 생각합니다.
{
    NodeType<ItemType>* minPtr = MinLoc(location, location);
    ItemType temp;
    if (location != NULL)
    {
        temp = location->info;
        location->info = minPtr->info;
        minPtr->info = temp;
        Sort(location->next);
    }
    else
        return;
}

template <class ItemType>
NodeType<ItemType>* UnsortedType<ItemType>::get_listData() {
    return listData;
}

template <class ItemType>
void UnsortedType<ItemType>::Print() {
    NodeType<ItemType>* temp_ptr = listData;
    while (temp_ptr != NULL) {
        cout << temp_ptr->info << " ";
        temp_ptr = temp_ptr->next;
    }
}