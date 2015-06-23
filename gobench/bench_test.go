package gobench

import (
	"testing"
)

func BenchmarkGoGeneric(b *testing.B) {
	for i := 0; i < b.N; i++ {
		GoGeneric()
	}
}

func BenchmarkGoSpecific(b *testing.B) {

	for i := 0; i < b.N; i++ {
		GoSpecific()
	}

}
func BenchmarkGoMapAdd(b *testing.B) {

	for i := 0; i < b.N; i++ {
		GoMapAdd()
	}

}
func BenchmarkGoStructAdd(b *testing.B) {

	for i := 0; i < b.N; i++ {
		GoStructAdd()
	}

}
