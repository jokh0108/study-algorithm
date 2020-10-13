#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> numbers)
{
    set<int> s;

    for (int i = 0; i < numbers.size(); i++)
    {
        for (int j = i + 1; j < numbers.size(); j++)
        {
            s.insert(numbers[i] + numbers[j]);
        }
    }

    vector<int> answer(s.begin(), s.end());

    sort(answer.begin(), answer.end());

    return answer;
}

int main()
{
    auto numbers = vector<int>{2, 1, 3, 4, 1};
    for (auto &&i : solution(numbers))
    {
        std::cout << i << ' ';
    }
    auto numbers2 = vector<int>{5, 0, 2, 7};
    for (auto &&i : solution(numbers2))
    {
        std::cout << i << ' ';
    }

    return 0;
}
