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
// ���� ���� �Լ��� ���̸� ���� ���ϰ� ����� return�ϹǷ�
// ���̰� �ٸ� ��� ����ð��� �� ª�� �ɸ��ϴ�.
// ���̰� ���� ��� list�� item�� ���� ������ �� tree�� �����۰� ���ϴ�
// ���� ���� ����� �ð��� �� ª�� �ɸ��ϴ�.
// tree�� ũ�⿡ ���� ���ĵǾ��ִٰ� �� �� �����Ƿ� O(logN)�� �ɸ�����
// tree�� item�� �̾� unsorted list�� item�� ���ϸ� O(N)�� �ɸ��ϴ�.


//�Ʒ� ������ ���� �� �� ����ð� �鿡�� ���� ���̰� ������?
tree.ResetTree(IN_ORDER); // tree�� iterator�� ����� �غ� �Ѵ�
for (int i = 0; i < list_length; i++) {
	tree.GetNextItem(item, IN_ORDER, found); // tree���� �ϳ��� �������� �����´�
	list.RetrieveItem(item, found); // list�� �ش� �������� �ִ� �˻�. O(N)�� �ɸ�.
	if (!found))
		return false;
}
*/