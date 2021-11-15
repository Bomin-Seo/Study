// The following declarations and definitions go into file 
// ItemType.h. 
#ifndef itemtype_h
#define itemtype_h
#include <fstream>
const int MAX_ITEMS = 5;
enum RelationType  {LESS, GREATER, EQUAL};

class ItemType 
{ 
public:
  ItemType();
  RelationType ComparedTo(ItemType) const;
  void Print(std::ostream&) const;
  void Initialize(int number);
  int getvalue() const;
private:
  int value;
};
#endif itemtype_h 
