package main

import (
	"testing"
)

func BenchmarkFibV1(b *testing.B) {
	// run the Fib function b.N times
	k := make(map[int]int)
	k[0] = 0
	k[1] = 1
	for n := 0; n < b.N; n++ {

		Fib(5, k)
	}
}
