#include<iostream>
#include<string>
using namespace std;
bool helpingFunction(string s,int start,int last)
{
	if(start==last || start>last)
	{
		return true;
	}
	bool is=helpingFunction(s,start+1,last-1);
	if(is)
	{
		if(s[start]==s[last])
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	else
	{
		return false;
	}
}
bool Ispalindrome(string s)
{
	int start=0,last=s.length()-1;
	return helpingFunction(s,start,last);
}
void main()
{
	string s="madam";
	bool is=Ispalindrome(s);
	if(is)
	{
		cout<<"Palindrome\n";
	}
	else
	{
		cout<<"Not Palindrome\n";
	}
	system("pause");
}