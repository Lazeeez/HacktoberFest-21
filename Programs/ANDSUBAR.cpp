#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n,a=1;
        cin>>n;
        if(n==1)
         cout<<1<<"\n";
        else{
        while(a*2<=n)
        a=a*2;
        int b=n-a+1;
        if(n==a)
        cout<<a/2<<"\n";
        else
        cout<<max(a/2,b)<<"\n";
    }
    }
	return 0;
}
