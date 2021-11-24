template <class ItemType>
void swap(ItemType& one, ItemType& two);

template<class ItemType>
// Assumes ItemType is either a built-in simple type or a class
// with overloaded relational operators.
struct HeapType
{
  void ReheapDown(int root, int bottom);
  void ReheapUp(int root, int bottom);
  ItemType* elements;   // Array to be allocated dynamically
  int numElements;
};

template <class ItemType>
void Swap(ItemType& one, ItemType& two)
{
  ItemType temp;
  temp = one;
  one = two;
  two = temp;
}  
// ---------------- A번 ---------------------
template<class ItemType>
void HeapType<ItemType>::ReheapDown(int root, int bottom)
// Post: Heap property is restored.
{
    int maxChild;
    int rightChild;
    int leftChild;

    leftChild = root * 2 + 1;
    rightChild = root * 2 + 2;
    while (leftChild <= bottom) {
        if (leftChild == bottom)
            maxChild = leftChild;
        else
        {
            if (elements[leftChild] <= elements[rightChild])
                maxChild = rightChild;
            else
                maxChild = leftChild;
        }
        if (elements[root] < elements[maxChild])
        {
            Swap(elements[root], elements[maxChild]);
            root = maxChild;
            leftChild = root * 2 + 1;
            rightChild = root * 2 + 2;
        }
        else break;
    }
}
// ---------------- B번 ---------------------
template<class ItemType>
void HeapType<ItemType>::ReheapUp(int root, int bottom)
// Post: Heap property is restored.
{
    int parent;
    while (bottom > root) {
        parent = (bottom - 1) / 2;
        if (elements[parent] < elements[bottom]) {
            Swap(elements[parent], elements[bottom]);
            bottom = parent;
        }
        else break;
    }
}

/*------------------C번------------------------
A번의 Big-O는 O(logN)입니다.
leftchild와 rightchild를 지정하고, root를 새로 지정하며,
다시 root와 maxchild를 비교하여 swap하는 과정은 모두 O(1)이며
이와 같은 과정을 총 logN번 시행합니다.

B번의 Big-O는 O(logN)입니다.
parent를 지정하고 bottom값과 비교하고, swap하는 과정 모두 O(1)이며,
이와 같은 과정을 총 logN번 시행합니다.
*/