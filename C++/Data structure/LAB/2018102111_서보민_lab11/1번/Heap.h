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
// ---------------- A�� ---------------------
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
// ---------------- B�� ---------------------
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

/*------------------C��------------------------
A���� Big-O�� O(logN)�Դϴ�.
leftchild�� rightchild�� �����ϰ�, root�� ���� �����ϸ�,
�ٽ� root�� maxchild�� ���Ͽ� swap�ϴ� ������ ��� O(1)�̸�
�̿� ���� ������ �� logN�� �����մϴ�.

B���� Big-O�� O(logN)�Դϴ�.
parent�� �����ϰ� bottom���� ���ϰ�, swap�ϴ� ���� ��� O(1)�̸�,
�̿� ���� ������ �� logN�� �����մϴ�.
*/