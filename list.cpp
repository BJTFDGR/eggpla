#include "stdafx.h"
#include "list.h"

template<class type>//��֪��дʲô��Ϊhead tail����ռ䣬�������һ��
linklist<type>::linklist()
{
	head = new node;
	tail = new node;
	head->next = tail;
	tail->prev = head;
	currentlength = 0;//��д��
}

template<class type>
linklist<type>::~linklist()
{
	clear();
	delete head;
	delete tail;
}





template<class type>
 void linklist<type>::clear()
{
	 node*tmp = head->next;
	 head->next = tail;
	 tail->prev = head;
	 while (tmp!= tail)//���α��ϲ�̫һ��
	 {
		 tmp = tmp->next;
		 delete tmp->prev;
	 }
	 currentlength = 0;//ע������,��д��
}

 template<class type>
 int linklist<type>::length() const
 {
	 return currentlength;
 }

 template<class type>//�嵽iǰ�滹��i���棿 ��i��i-1
 void linklist<type>::insert(int i, const type & x)
 {
	 node*p = move(i);
	 node*tmp = new node(x, p, p->prev);
	 p->prev->next = tmp;
	 p->prev = tmp;

	 currentlength++;//ע������,��д��
 }

 template<class type>
 void linklist<type>::remove(int i)
 {
	 char*tmp = move(i);
	 tmp->next->prev = tmp->prev;
	 tmp->prev->next = tmp->next;//�����¸��ṹ��ĵ�ַ��ʵ�Ͼ����¸��ṹ���ָ��

	 delete tmp;//��������һ���й����ʣ���ʵ��ɾ��ָ����Զ����ö�Ӧ����������

	 currentlength--;
 }

 template<class type>
 int linklist<type>::search(const type & x) const
 {
	 node*tmp = head;
	 int i = 0;

	 while (tmp != tail && tmp->data != x)
	 {
		 tmp = tmp->next;
		 i++;
	 }

	 if (tmp == tail)
	 {
		 cout << "none exit\t\n";
		 return -1;
	 }
	 else return i;//same question,should i start from 0?

	 return 0;
 }

 template<class type>
 type linklist<type>::visit(int i) const
 {
	 if (i<0 || i>currentlength)throw OutOfBound();//at first,this hacebeen ignorant

	 node*tmp=head;
	 int n = 0;
	 while (n < i)
	 {
		 tmp = tmp->next;
		 n++;
	 }

	 return tmp->data;//��Ҳ��֪��Ӧ����ǰһ�����Ǻ�һ��
 }

 template<class type>
 void linklist<type>::traverse() const
 {
	 node*tmp = head-next;
	 while (node != tail)
	 {
		 cout << tmp->data << endl;
		 tmp = tmp->next;
	 }

 }


