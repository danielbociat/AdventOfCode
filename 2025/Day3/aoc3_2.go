package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	sum := 0

	rows := 13

	for scanner.Scan() {
		line := scanner.Text()

		n := len(line)
		mat := make([][]int, 13)
		for i := 0; i < rows; i++ {
			mat[i] = make([]int, n)

			for j := 0; j < n; j++ {
				mat[i][j] = -1
			}
		}

		mat[1][n-1] = int(line[n-1] - '0')
		for j := n - 2; j >= 0; j-- {
			mat[1][j] = max(int(line[j]-'0'), mat[1][j+1])
			// fmt.Println(1, j, line, mat[1][j])
		}

		for i := 2; i <= 12; i++ {
			for j := 0; j < n-1; j++ {
				mat[i][j], _ = strconv.Atoi(strconv.Itoa(int(line[j]-'0')) + strconv.Itoa(mat[i-1][j+1]))
				// fmt.Println(i, j, line, mat[i][j])
			}
			for j := n - 2; j >= 0; j-- {
				mat[i][j] = max(mat[i][j], mat[i][j+1])
			}
		}

		maxi := mat[12][0]
		sum += maxi

	}

	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
