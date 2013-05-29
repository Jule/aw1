package main

import (
    "fmt"
    "time"
)

func stage1(in chan int, out chan int) {
    for {
        current := <- in
        op := current * 2
        out <- op
    }
}

func stage2(in chan int, out chan int) {
    for {
        current := <- in
        fmt.Println("Value: ", current)
    }
}

func main() {
    stage1_in := make(chan int)
    stage1_out := make(chan int)

    /*values := [4]int{1, 2, 3, 4}
    for _, element := range values {
        stage1_in <- element
    }*/

    go func() {
        for _, element := range [4]int{1, 2, 3, 4} {
            stage1_in <- element
        }
    }()

    go stage1(stage1_in, stage1_out)
    go stage2(stage1_out, nil)

    for { time.Sleep(1 * time.Second) }
}


