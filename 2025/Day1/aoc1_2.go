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

	current := 50

	val := 0
	counter := 0
	movement := 1

	for scanner.Scan() {
		rotation := scanner.Text()

		val, _ = strconv.Atoi(rotation[1:])

		counter += val / 100
		val %= 100

		if rotation[0] == 'L' {
			if val > current && current != 0 {
				counter++ // extra click
			}
			movement = -1
		} else {
			if val > 100-current {
				counter++

			}
			movement = 1
		}

		current = (100 + current + movement*val) % 100

		if current%100 == 0 {
			counter++
		}
	}

	fmt.Println(counter)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
