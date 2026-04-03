#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long N;
    vector<long long> factors;
    cin >> N;

    for (long long i = 2; i * i <= N; i++)
    {
        while (N % i == 0)
        {
            factors.push_back(i);
            N /= i;
        }
    }

    if (N > 1)
        factors.push_back(N);

    for (int i = 0; i < factors.size(); i++)
    {
        cout << factors[i];
        if (i != factors.size() - 1)
            cout << " * ";
    }
    cout << endl;

    return 0;
}
