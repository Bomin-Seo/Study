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
  void PrintSumSquares();
private:
  NodeType<ItemType>* listData;
  int length;
  NodeType<ItemType>* currentPos;
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
// Class destructor
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
void UnsortedType<ItemType>::PrintSumSquares()
{
    //a, b, c, d, e의 문제를 수정 후 출력
    cout << SumSquares_a(listData) << endl; // a 번 함수
    cout << SumSquares_b(listData) << endl; // b 번 함수
    cout << SumSquares_c(listData) << endl; // c 번 함수
    cout << SumSquares_d(listData) << endl; // d 번 함수
    cout << SumSquares_e(listData) << endl; // e 번 함수
};

template <class ItemType>
ItemType SumSquares_a(NodeType<ItemType>* list)
// Base case를 명확하게 설정하지 않아 에러가 발생합니다.
// 수정 전에는 함수가 실행되면 바로 0을 return하기 때문에 제대로 동작하지 않습니다.
{
    if (list == NULL)
        return 0;
    else
        return (list->info * list->info) + SumSquares_a(list->next);
}

template <class ItemType>
ItemType SumSquares_b(NodeType<ItemType>* list)
// 수정 전에는 list->info의 총합을 구하는 함수입니다.
// 제곱의 합을 도출하도록 동작하기 위하여 list->info를 곱한 뒤 더해줍니다.
{
    int sum = 0;
    while (list != NULL) {
        sum = list->info * list->info + sum;
        list = list->next;
    }
    return sum;
}

template <class ItemType>
ItemType SumSquares_c(NodeType<ItemType>* list)
// 잘못된 부분이 없습니다.
{
    if (list == NULL)
        return 0;
    else
        return list->info * list->info + SumSquares_c(list->next);
}

template <class ItemType>
ItemType SumSquares_d(NodeType<ItemType>* list)
// 잘못된 부분이 없습니다.
{
    if (list->next == NULL)
        return list->info * list->info;
    else
        return list->info * list->info + SumSquares_d(list->next);
}

template <class ItemType>
ItemType SumSquares_e(NodeType<ItemType>* list)
// 수정 전에는 info가 아닌 node자체를 곱하며
// 또한 info 제곱의 합의 총합을 도출하는 부분 또한 없습니다.
{
    if (list == NULL)
        return 0;
    else
        return SumSquares_e(list->next) + list->info * list->info;
}
