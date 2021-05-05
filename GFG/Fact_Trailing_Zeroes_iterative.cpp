#include<bits/stdc++.h>
using namespace std;
// program to calculate trailing zeroes in a factorial
int main(){
  ios_base :: sync_with_stdio(false);
  cin.tie(NULL);

  long long n,fact=1,count=0;
  cin>>n;
  
  for (int i=2;i<=n;i++){
    fact = fact*i;
  }

  while(fact%10 ==0){
    count++;
    fact/=10;
  }
  cout<<"Trailing zeroes in factorial of "<<n<<" are "<<count;
  return 0;
}
