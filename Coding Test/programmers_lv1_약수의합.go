package main

import "fmt"

func solution(n int) int {
	answer := n
	for i := 1; i < n; i++ {
		if n%i == 0 {
			answer += i
		}
	}
	return answer
}

func main() {
	n := 12
	fmt.Println(solution(n))
}
