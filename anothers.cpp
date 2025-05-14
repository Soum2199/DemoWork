// Powers of two Coderbyte
#include <iostream>
#include <string>
using namespace std;

int PowersofTwo(int num) {
   
  // return num;
  if(num == 1) return true;
  if(num<=0 || num%2!=0) return false;
  return PowersofTwo(num/2);
}

// keep this function call here
int main(void) { 
   
  cout << PowersofTwo(coderbyteInternalStdinFunction(stdin));
  return 0;
}