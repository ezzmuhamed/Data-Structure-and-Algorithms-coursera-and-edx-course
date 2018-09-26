

#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;

int max_product (const vector<int>&number)
{
	int result = 0;
	int n = number.size();
	for(int i =0 ; i<n ; i++)
	{
		for(int j = i+1; j<n ; j++)
		{
			if(number[i] * number[j] > result)
			{
				result = number[i] * number[j] ;

			}
		}
	}
	return result ;
}


long long max_product_fast(const vector<int>&number)
{
	int n = number.size();
	signed int max_index1 = -1;
	for (int i=0; i<n;++i)
		if((max_index1 == -1 )  ||  number[i] > number[max_index1])
		  max_index1 = i ;

	signed int max_index2 = -1;
	for(int j = 0; j<n; ++j)
		if((j != max_index1) && ((max_index2 == -1 )  ||  (number[j] > number[max_index2])))
		  max_index2 = j ;
  
	return ((long long)(number[max_index1])) *  number[max_index2];

}

int main()
{
	int n ;
	cin >> n;
	vector<int>number(n);
	for(int i = 0;i<n;++i)
	{
       cin >> number[i];
	
	}
    long long result = max_product_fast(number);
	cout<< result ;
	system("pause");
	return 0;

}
