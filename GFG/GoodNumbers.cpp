#include <iostream>
using namespace std;

#include <bits/stdc++.h>
using namespace std;

int main(){
    
    long long T;
    cin>>T;
    while(T--)
{
  long long num,rem,sum=0;
  cin>>num;
  int i=0;
  while(i<10){
  if(num%10 ==num) break;
  while(num){
  rem = num%10;
  sum +=rem;
  num /= 10;}
  
  num = sum;
  sum=0;
  i++;
  }
  printf("%lld\n",num);
  
}
return 0;
    
}
