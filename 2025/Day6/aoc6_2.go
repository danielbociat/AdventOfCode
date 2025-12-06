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

	var data []string

	var sol int64 = 0

	for scanner.Scan() {
		line := scanner.Text()

		if line == "" {
			break
		}

		data = append(data, line)
	}

	rows := len(data)
	cols := len(data[0])

	//var temp int64 = 0
	fmt.Println(data)
	var nums []int64

	for j := cols - 1; j >= 0; j-- {
		var curr int64 = 0

		for i := 0; i < rows-1; i++ {
			if data[i][j] != ' ' {
				val := int64(data[i][j] - '0')
				curr = curr*10 + val
			}
		}

		nums = append(nums, curr)

		if data[rows-1][j] == '+' {
			fmt.Println(nums)
			temp := int64(0)

			for _, val := range nums {
				temp = temp + val
			}

			sol += temp
			nums = make([]int64, 0)
			j--
		} else if data[rows-1][j] == '*' {
			fmt.Println(nums)
			temp := int64(1)

			for _, val := range nums {
				temp = temp * val
			}

			sol += temp
			nums = make([]int64, 0)
			j--
		}
	}

	fmt.Println(sol)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
