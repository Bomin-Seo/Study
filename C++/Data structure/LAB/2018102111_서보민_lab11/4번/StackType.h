typedef int ItemType;
struct NodeType;

class FullStack
{};
class EmptyStack
{};


class StackType
{
public:
  StackType();
  ~StackType();
  bool IsFull() const;
  bool IsEmpty() const;
  void Push(ItemType item);
  void Pop();
  ItemType Top();
private:
  NodeType* topPtr;
};

struct NodeType
{
  ItemType info;
  NodeType* next;
  int timestamp;
};

