#include <bits/stdc++.h>
using namespace std;

int main(){
    
    ios_base :: sync_with_stdio(false);
	cin.tie(NULL);
	long long T;
	cin>>T;
	while(T--){
	    long long N,K,s=0;
	    cin>>N>>K;
	    vector<long long> a(N);
	    for (int i=0;i<N;i++) {cin>>a[i];}
	    
	    sort(a.begin(),a.end());
	    int free_graphs = N/(K+1);
	    
	    N -= free_graphs;
	    
	    for (int i=0;i<N;i++){
	        s +=a[i];
	    }
	   // printf("%d\n",s);
	   cout<<s<<"\n";
	    
	}
	//code
	return 0;
}
