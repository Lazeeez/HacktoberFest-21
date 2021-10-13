#include<bits/stdc++.h>

int max(int a,int b)
{
    if(a<b)
    return b;
    return a;
}

int min(int a,int b)
{
    if(a<b)
    return a;
    return b;
}

int main()
{
    int f,i,j,k,len=0,temp;
    char a[100000],b[100000],c[100000],ch;
    
    //First String
    printf("Enter string 1:");
    scanf("%s",a);
    //Second String
    printf("Enter string 2:");
    scanf("%s",b);
    
    //To convert strings to uppercase
    for (int i = 0; i < strlen(a); i++) 
    {
        ch = toupper(a[i]);
        a[i] = ch;
    }
    for (int i = 0; i < strlen(b); i++) 
    {
        ch = toupper(b[i]);
        b[i] = ch;
    }
    
    const int m=strlen(a)+1;
    const int n=strlen(b)+1;
    int t[m][n];
    char d[m][n];
    for(i=0;i<=m;i++)
    {
        for(j=0;j<=n;j++)
        {
            t[i][j]=0;
        }
    }
    for(i=1;i<=m;i++)
    {
        for(j=1;j<=n;j++)
        {
            if(a[i-1]==b[j-1])
            {
                t[i][j]=1+t[i-1][j-1];
                d[i][j]='d';
            }
            else
            {
                t[i][j]=max(t[i-1][j],t[i][j-1]);
                if(t[i-1][j]>=t[i][j-1])
                {
                    t[i][j]=t[i-1][j];
                    d[i][j]='u';
                }
                else
                {
                    t[i][j]=t[i][j-1];
                    d[i][j]='l';
                }
            }
        }
    }
    printf("\n ");
    k=min(m,n);
    k--;
    i=m,j=n;
    while(i>0 && j>0)
    {
        if(d[i][j]=='d')
        {
            c[k]=a[i-1];
            len++;
            i--;
            j--;
            k--;
        }
        else if(d[i][j]=='u')
        {
            i--;
        }
        else
        {
            j--;
        }
    }
    temp=min(m,n);
    printf("Longest Common Sequence:");
    for(i=k;i<temp;i++)
    {
        printf("%c",c[i]);
    }
    return 0;
}