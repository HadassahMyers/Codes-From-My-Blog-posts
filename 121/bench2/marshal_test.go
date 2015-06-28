package bench2

import (
	"testing"
)

func BenchmarkMarshalMap(b *testing.B) {

	for i := 0; i < b.N; i++ {
		MarshalMap()
	}

}
func BenchmarkMarshalStruct(b *testing.B) {

	for i := 0; i < b.N; i++ {
		MarshalStruct()
	}

}
