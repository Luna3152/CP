#include <bits/stdc++.h>
using namespace std;

bool isprime(long long N)
{
    for (long long i = 2; i * i <= N; i++)
    {
        if (N % i == 0)
            return false;
    }
    return true;
}

int main()
{
    long long N;
    cin >> N;
    if (isprime(N))
    {
        cout << "prime" << endl;
    }
    else
    {
        cout << "not prime" << endl;
    }
}
