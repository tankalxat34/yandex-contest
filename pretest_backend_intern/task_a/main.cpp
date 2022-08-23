#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    long long a, b;
    cin >> a >> b;
    long long c = a + b;
    cout << c;
}