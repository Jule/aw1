func stage1(in chan int, out chan int) {
	for {
		current := <-in
		op := current * 2
		out <- op
	}
}

func stage2(in chan int, out chan int) {
	for {
		current := <-in
		fmt.Println("Value: ", current)
		out <- current
	}
}
