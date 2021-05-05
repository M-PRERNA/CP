#include<bits/stdc++.h>
using namespace std;
// efficient method to finding trailing zeroes
int main(){
  ios_base:: sync_with_stdio(false);
  cin.tie(NULL);
  long long n,count=0;
  cin>>n;
  // instead of calc the fact we find the no. of 5's
  // Time complexity is  O(logn)
  // space complexity O(1)
  for (long long i=5 ; i<=n ; i=i*5){
    count += n/i; //this itself is a floor value
  }
   cout<<"Trailing zeroes in "<<n<<" are "<<count;
  return 0;
}
