#include <bits/stdc++.h>
using namespace std;

double func(double x, double y)
{
	cout<<setprecision(13);
	return (x*x + y*y);
}

int main()
{
	double a= 2.12275418, b=4.82765928716;
	double c = func(a,b);
	// vector<vector<int>> v;
	cout<<c<<endl;
	return 0;
}

