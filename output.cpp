#include <iostream>
using namespace std;
int main(){
int fib = 0;
cin >> fib;
if(fib == 0) {
cout << 0 << endl;
} else if(fib == 1 or fib == 2) {
cout << 1 << endl;
} else {
int fib2 = 1;
int fib1 = 1;
int x = 0;
for(int i = 2;i < fib;i = i+1) {
x = fib2+fib1;
fib2 = fib1;
fib1 = x;
}
cout << x << endl;
}
return 0;
}
