package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var data [][]string

	var sol int64 = 0

	for scanner.Scan() {
		line := scanner.Text()

		if line == "" {
			break
		}

		elements := strings.Fields(line)
		data = append(data, elements)
	}

	rows := len(data)
	cols := len(data[0])

	var temp int64 = 0
	fmt.Println(data)
	for j := 0; j < cols; j++ {
		if data[rows-1][j] == "+" {
			temp = 0
		} else {
			temp = 1
		}

		for i := 0; i < rows-1; i++ {
			val, _ := strconv.ParseInt(data[i][j], 10, 64)
			if data[rows-1][j] == "+" {
				temp += val
			} else {
				temp *= val
			}
		}

		sol += temp
	}

	fmt.Println(sol)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
