// Create a channel with a capacity of one
channel := make(chan int, 2)
channel <- 5       // Write data to a channel
out := <- channel  // Retrieve data
