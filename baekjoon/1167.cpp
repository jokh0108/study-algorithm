#include <iostream>
#include <vector>

using namespace std;
int n;
vector<pair<int, int>> graph;

int main() {
    
	cin >> n;
	graph.resize(n + 1);
	int temp, node, edge;
	for (int i = 0; i < n; i++)
	{
		cin >> temp;
		while (true) {
			cin >> node;
			if (node == -1) break;
			cin >> edge;
			pair<int, int> leaf;
			leaf.first = node;
			leaf.second = edge;
			graph.push_back(leaf);
		}
	}
	cout << "h";
	return 0;
}