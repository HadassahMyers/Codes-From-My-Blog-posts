package main

import "fmt"

func main() {
	var fibMap map[int]int
	fibMap = make(map[int]int)
	fibMap[0] = 0
	fibMap[1] = 1

	fmt.Println(Fib(20, fibMap))
}
func Fib(n int, fibMap map[int]int) int {

	if val, ok := fibMap[n]; ok {
		return val
	}
	fibMap[n] = Fib(n-1, fibMap) + Fib(n-2, fibMap)

	return fibMap[n]
}
