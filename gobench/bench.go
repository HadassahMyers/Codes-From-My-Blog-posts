package gobench

func GoGeneric() {
	i := 10
	j := 20
	_ = i + j

}

func GoSpecific() {
	var (
		i int = 10
		j int = 20
	)
	_ = i + j
}

func GoMapAdd() {
	m := map[int]int{0: 0, 1: 1}
	_ = m[0] + m[1]
}

func GoStructAdd() {
	m := struct{ a, b int }{0, 1}
	_ = m.a + m.b
}
