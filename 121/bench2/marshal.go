package bench2

import (
	"encoding/json"
)

func MarshalMap() {
	m := map[int]int{0: 0, 1: 1}
	json.Marshal(m)
}

func MarshalStruct() {
	m := struct{ a, b int }{0, 1}
	json.Marshal(m)
}
