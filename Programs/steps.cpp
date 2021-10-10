#include<iostream>
using namespace std;
int main ()
{
  for (int i = 0; i < 5; ++i)
    {
      for (int j = i; j < 5; ++j)
	{
	 cout << " ";
	}
      {
	for (int k = 0; k < i; ++k)
	  cout << "#";
      }
	  cout <<endl;
    }
}
