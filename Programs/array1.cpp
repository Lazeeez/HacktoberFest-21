#include<iostream>

bool anai(int n)
{
    // bool ans; // 0-150
    // if(n%7==0){
    //     ans=true;
    // } 
    // else{
    //     ans = false;
    // }
    // return ans;
    return true ? (n%7==0) : false;
}


int main()
{
  for(int i = 0 ; i < 151 ; i++){

  
  if(anai(i)==1){
      std::cout << i << std::endl;
  }
}
}
