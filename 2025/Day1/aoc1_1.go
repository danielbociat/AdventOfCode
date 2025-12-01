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
	movement := 1
	val := 0
	counter := 0

	for scanner.Scan() {
		rotation := scanner.Text()
		if rotation[0] == 'L' {
			movement = -1
		} else {
			movement = 1
		}

		val, _ = strconv.Atoi(rotation[1:])

		current = (current + movement*val) % 100

		if current == 0 {
			counter++
		}
	}

	fmt.Println(counter)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
