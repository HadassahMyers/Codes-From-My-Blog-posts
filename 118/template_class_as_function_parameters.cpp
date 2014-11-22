#include <iostream>

template<class Type>
class Other {
    
    public:
    	Type x;
    	Other(Type y){
        	x = y;
    	}
};



    void first(const Other<int>& o) {/*One way of specifying the formal parameter*/
    	
    	std::cout << o.x << '\n';
    }
        
 

    template<typename T> void second(const Other<T>& o) {/*Other way of specifyin formal parameter*/
    	/*Has to be decalred as templated function*/
        std::cout << o.x << '\n';
    }


int main(){
    Other<int> other(123);/*initializing template class constructor*/
    first(other);/*sending templated class as parameters*/
    second(other);
}
