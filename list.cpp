#include "stdafx.h"
#include "list.h"

template<class type>//不知道写什么？为head tail申请空间，随后再连一起
linklist<type>::linklist()
{
	head = new node;
	tail = new node;
	head->next = tail;
	tail->prev = head;
	currentlength = 0;//忘写了
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
	 while (tmp!= tail)//跟课本上不太一样
	 {
		 tmp = tmp->next;
		 delete tmp->prev;
	 }
	 currentlength = 0;//注意清零,忘写了
}

 template<class type>
 int linklist<type>::length() const
 {
	 return currentlength;
 }

 template<class type>//插到i前面还是i后面？ 是i和i-1
 void linklist<type>::insert(int i, const type & x)
 {
	 node*p = move(i);
	 node*tmp = new node(x, p, p->prev);
	 p->prev->next = tmp;
	 p->prev = tmp;

	 currentlength++;//注意清零,忘写了
 }

 template<class type>
 void linklist<type>::remove(int i)
 {
	 char*tmp = move(i);
	 tmp->next->prev = tmp->prev;
	 tmp->prev->next = tmp->next;//放上下个结构体的地址事实上就是下个结构体的指针

	 delete tmp;//曾经在这一块有过疑问，事实上删除指针会自动启用对应的析构函数

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

	 return tmp->data;//我也不知道应该是前一个还是后一个
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


