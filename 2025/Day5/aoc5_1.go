package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Pair struct {
	A int64
	B int64
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	flag := false
	var pairs []Pair
	sol := 0

	for scanner.Scan() {
		line := scanner.Text()

		if line == "" {
			flag = true
		} else {
			if flag {
				nr, _ := strconv.ParseInt(line, 10, 64)
				for i := range pairs {
					if nr >= pairs[i].A && nr <= pairs[i].B {
						sol++
						break
					}
				}
			} else {
				bounds := strings.SplitN(line, "-", 2)

				x, _ := strconv.ParseInt(bounds[0], 10, 64)
				y, _ := strconv.ParseInt(bounds[1], 10, 64)

				pairs = append(pairs, Pair{x, y})
			}
		}
	}

	fmt.Println(sol)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
