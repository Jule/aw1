func main() {
	N := 100 // Number of elements to process

	stage1_in := make(chan int)
	stage1_out := make(chan int)
	stage2_out := make(chan int)

	go func() {
		// Send N integers to the
		// stage1_in channel
	}()

	go stage1(stage1_in, stage1_out)
	go stage2(stage1_out, stage2_out)

	// Wait for all elements to be processed
	for i := 0; i < N; i++ {
		<-stage2_out
	}
}
