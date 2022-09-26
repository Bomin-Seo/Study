package main

func solution(arr []int) float64 {
	sum := float64(0)
	for i := 0; i < len(arr); i++ {
		sum = sum + float64(arr[i])
	}
	sum /= float64(len(arr))

	return float64(sum)
}

func main() {
	arr := []int{1, 2, 3, 4}
	solution(arr)
}
