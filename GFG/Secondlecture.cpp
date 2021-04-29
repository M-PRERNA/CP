#include <bits/stdc++.h>
using namespace std;

int main() {
	//code
	ios_base :: sync_with_stdio(false);
	cin.tie(NULL);
	long long T,N;
	cin>>T;
	while (T--){
	    cin>>N;
	    if ((2*N+1) % 3 == 0){
	        cout<<std::fixed;
	        cout<<std::setprecision(0);
	        cout<<"YES "<<(2*N+1) / 3<<"\n";
	    }
	    else {cout<<"NO"<<"\n";}
	}
	
	return 0;
}
