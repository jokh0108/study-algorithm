#include <iostream>
#include <utility>
#include <vector>
#include <random>
#include <map>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
    pair<int, int> p;
    p = make_pair(5, 3);
    cout << p.first << p.second << '\n';

    vector<int> v1(3);
    cout << v1[0] << '\n';

    vector<int> v2(10);
    for (int i = 0; i < v2.size(); i++)
    {
        v2[i] = rand() % 10;
        cout << v2[i] << ' ';
    }
    cout << '\n';
    cout << '\n';
    cout << '\n';
    reverse(v2.begin(), v2.end());
    cout << "reverse\n";
    
    for (vector<int>::iterator i = v2.begin(); i < v2.end(); i++)
    {
        cout << *i << ' ';
    }
    cout << '\n';
    cout << "reverse 3 to end\n";

    reverse(v2.begin() + 3, v2.end());
    for (vector<int>::iterator i = v2.begin(); i < v2.end(); i++)
    {
        cout << *i << ' ';
    }
    cout << '\n';
    cout << "sort\n";
    
    sort(v2.begin(), v2.end());
    for (vector<int>::iterator i = v2.begin(); i < v2.end(); i++)
    {
        cout << *i << ' ';
    }
    cout << '\n';
    cout << "sort again\n";

    sort(v2.begin(), v2.end());
    for (vector<int>::iterator i = v2.begin(); i < v2.end(); i++)
    {
        cout << *i << ' ';
    }
    cout << '\n';
    cout << "sort 3 to end\n";

    sort(v2.begin() + 3, v2.end());
    for (vector<int>::iterator i = v2.begin(); i < v2.end(); i++)
    {
        cout << *i << ' ';
    }
    cout << '\n';

    int n = 10;
    int m = 10;

    vector<vector<int>> v3(n, vector<int>(m, 0));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            v3[i][j] = rand() % 10;
            cout << v3[i][j] << ' ';
        }
        cout << '\n';
    }

	//int 자료형을 key로 int 자료형을 데이터로 저장하는 딕셔너리 자료구조 생성
	map<int, int> dict;
	//(4, 5)원소 삽입
	dict.insert(make_pair(4, 5));
	//또는
	dict[5]=6;
	//key와 연관된 원소를 pair<키 자료형, 데이터 자료형> 형태로 리턴함
	// printf("%d\n", dict.find(4)->second);
	// //key와 연관된 원소의 개수를 리턴함
	// printf("%d\n", dict.count(4));
	// //저장된 원소의 수를 리턴함
	// printf("%d\n", dict.size());
    for (map<int, int>::iterator i = dict.begin(); i != dict.end(); i++)
    {
        cout << '['<< i->first << " : " <<i->second<<"]" << '\n';
    }
    cout << '\n';
    return 0;
}