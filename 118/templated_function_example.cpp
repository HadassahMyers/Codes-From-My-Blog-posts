#include <iostream>
#include <typeinfo>
using namespace std;
template <typename Type> void test_template(Type x){
    cout << x <<endl;
    cout << typeid(Type).name() << endl;
}
int main()
{
   
   test_template<int>(2);
   test_template<double>(3.0);
   return 0;
}
