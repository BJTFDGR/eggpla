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
	virtual int search(const type&x)const = 0;//һ��ʼ��Ϊ���������ýṹ�е�����
	virtual type visit(int i)const = 0;//���ں��治���޸�����
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
	struct node//���structʵ�����Ǹ�class,ע�⹹�캯��
	{
		type data;
		node*next,*prev;
		node() :next(NULL), prev(NULL) {};
		node(const type& x, node*m, node*n)
		{
			data = x; next = m; prev = n;
		}
		~node() {};//�Ҿ�˵������������
	};

	//partII
	node*head, *tail;
	int currentlength;

	//partIII ��д�������������ô����ͨ��
	node* move(int i)const
	{
		if (i<0 || i>currentlength)
			throw OutOfBound();	//at first,this hacebeen ignorant

		node*tmp = head;
		while (i>0)
		{
			tmp = tmp->next;
			i--;
		}//Ӧ�ÿ����ǲ����ƶ�����i���ڵ��ˣ��и����⣬head�ǵ�0���ǵ�һ��
		return tmp;
	}

public:

	linklist();
	~linklist();

	  void clear() ;
	  int length()const ;
	  void insert(int i, const type&x) ;
	  void remove(int i) ;
	  int search(const type&x)const ;//һ��ʼ��Ϊ���������ýṹ�е�����
	  type visit(int i)const ;//���ں��治���޸�����
	  void traverse()const ;

};



#endif

