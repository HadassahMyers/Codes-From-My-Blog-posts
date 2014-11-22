
#include <iostream>
using namespace std;
template <typename Type> class calc{
	public:
		Type multiply(Type x,Type y);
		Type add(Type x,Type y);
};

template <typename Type> Type calc<Type>::add(Type x,Type y)
{
	return x+y;
}

template <typename Type> Type calc<Type>::multiply(Type x,Type y)
{
	return x*y;
}
int main(){
	calc<int> instance1;
	calc<double> instance2;
	cout<<instance1.add(2,5)<<endl;
	cout<<instance2.multiply(3.0,5.0)<<endl;

}
