#include <iostream>
#include "TreeType.h"
#include "UnsortedType.h"

bool MatchingItem_Unsorted(TreeType& tree, UnsortedType<ItemType>& list)
{
	int list_length = list.LengthIs();
	int tree_length = tree.LengthIs();
	if (list_length != tree_length)
	{
		return false;
	}
	else
	{
		ItemType item;
		bool found;
		list.ResetList();
		for (int i = 0; i < list_length; i++) {
			list.GetNextItem(item); 
			tree.RetrieveItem(item, found); 
			if (!found)
				return false;
		}
		return true;
	}
}
/*
// 먼저 앞의 함수는 길이를 먼저 비교하고 결과를 return하므로
// 길이가 다른 경우 수행시간이 더 짧게 걸립니다.
// 길이가 같은 경우 list의 item을 먼저 가져온 후 tree의 아이템과 비교하는
// 앞의 구현 방식이 시간이 더 짧게 걸립니다.
// tree는 크기에 따라 정렬되어있다고 할 수 있으므로 O(logN)가 걸리지만
// tree의 item을 뽑아 unsorted list의 item과 비교하면 O(N)이 걸립니다.


//아래 구현과 비교해 볼 때 수행시간 면에서 무슨 차이가 있을까?
tree.ResetTree(IN_ORDER); // tree에 iterator를 사용할 준비를 한다
for (int i = 0; i < list_length; i++) {
	tree.GetNextItem(item, IN_ORDER, found); // tree에서 하나의 아이템을 가져온다
	list.RetrieveItem(item, found); // list에 해당 아이템이 있는 검색. O(N)이 걸림.
	if (!found))
		return false;
}
*/