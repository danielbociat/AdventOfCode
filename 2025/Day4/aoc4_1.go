package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

var dx = [8]int{-1, -1, -1, 0, 0, 1, 1, 1}
var dy = [8]int{0, 1, -1, 1, -1, 0, 1, -1}

func count(field []string, i int, j int) int {
	n := len(field)
	m := len(field[0])

	cnt := 0

	for k := 0; k < 8; k++ {
		newX := i + dx[k]
		newY := j + dy[k]

		if newX >= 0 && newX < n && newY >= 0 && newY < m && field[newX][newY] == '@' {
			cnt++
		}
	}

	return cnt
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	field := make([]string, 0)

	for scanner.Scan() {
		line := scanner.Text()
		field = append(field, line)
	}

	n := len(field)
	m := len(field[0])

	sol := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if field[i][j] == '@' && count(field, i, j) < 4 {
				sol++
			}
		}
	}

	fmt.Println(sol)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
