#include<iostream>

int
main ()
{
  for (int i = 0; i < 5; ++i)
    {

      for (int j = i; j < 5; ++j)
	{
	  std::cout << " ";

	}
      {
	for (int k = 0; k < i; ++k)
	  std::cout << "#";
      }

      std::cout << std::endl;

    }
}
