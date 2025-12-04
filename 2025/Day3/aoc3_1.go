package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	sum := 0

	for scanner.Scan() {
		line := scanner.Text()

		n := len(line)
		array := make([]int, n)
		for i := range array {
			array[i] = -1
		}

		array[n-1] = int(line[n-1] - '0')
		for i := n - 2; i >= 0; i-- {
			num := int(line[i] - '0')
			array[i] = max(array[i+1], num)
		}

		maxi := 0
		for i := 0; i < n-1; i++ {
			num := int(line[i] - '0')
			maxi = max(maxi, num*10+array[i+1])
		}
		sum += maxi
	}

	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
