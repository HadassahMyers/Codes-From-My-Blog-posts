
#include <iostream>
using namespace std;
class calculator {
    public:
		int add(int x,int y);
		int multiply(int x,int y);
	
};  

int calculator::add(int x,int y){
	return x+y;
}

int calculator::multiply(int x,int y){
	return x*y;
}
int main(){
    calculator instance;
    cout<<instance.add(1,2)<<endl;
    cout<<instance.multiply(5,2)<<endl;
}
