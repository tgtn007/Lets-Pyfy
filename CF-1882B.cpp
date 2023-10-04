#include <bits/stdc++.h>
using namespace std;
const int maxn=55;
bitset<maxn> s[maxn],tmp,all;
int t,n,k,x;
int main()
{
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(int i=1;i<maxn;i++)s[i].reset();
		all.reset();
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&k);
			while(k--)scanf("%d",&x),s[i][x]=1;
			all|=s[i];
		}
		int ans=0;
		for(int i=1;i<=50;i++)//哪个元素不要 
		{
			if(!all.test(i))continue;
			tmp.reset();
			for(int j=1;j<=n;j++)if(!s[j].test(i))tmp|=s[j];
			ans=max(ans,(int)tmp.count());
		}
		printf("%d\n",ans);
	}
	return 0;
}