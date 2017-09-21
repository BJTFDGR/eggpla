#include"stdafx.h"
#include"targetver.h"
#ifndef list_h
#define list_h
#include<iostream>
using namespace std;

#pragma once

template <class type>
class list
{
public://virtual function shall be put into public
	
	virtual void clear() = 0;
	virtual int length()const = 0;
	virtual void insert(int i,const type&x) = 0;
	virtual void remove(int i) = 0;
	virtual int search(const type&x)const = 0;//一开始以为是用来调用结构中的数字
	virtual type visit(int i)const = 0;//加在后面不会修改数据
	virtual void traverse()const = 0;
	

	virtual ~list();
};

class OutOfBound {};
class IllegalSize {};



template <class type>
class linklist :public list<type>//<type>
{
private:

	//part I
	struct node//这个struct实际上是个class,注意构造函数
	{
		type data;
		node*next,*prev;
		node() :next(NULL), prev(NULL) {};
		node(const type& x, node*m, node*n)
		{
			data = x; next = m; prev = n;
		}
		~node() {};//我就说不用析构函数
	};

	//partII
	node*head, *tail;
	int currentlength;

	//partIII 不写成内置类编译怎么都不通过
	node* move(int i)const
	{
		if (i<0 || i>currentlength)
			throw OutOfBound();	//at first,this hacebeen ignorant

		node*tmp = head;
		while (i>0)
		{
			tmp = tmp->next;
			i--;
		}//应该看看是不是移动到第i个节点了，有个问题，head是第0还是第一？
		return tmp;
	}

public:

	linklist();
	~linklist();

	  void clear() ;
	  int length()const ;
	  void insert(int i, const type&x) ;
	  void remove(int i) ;
	  int search(const type&x)const ;//一开始以为是用来调用结构中的数字
	  type visit(int i)const ;//加在后面不会修改数据
	  void traverse()const ;

};



#endif

