package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Pair struct {
	A int64
	B int64
}

func mergeIntervals(pairs []Pair) []Pair {
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].A < pairs[j].A
	})

	merged := []Pair{pairs[0]}

	for _, cur := range pairs[1:] {
		last := &merged[len(merged)-1]

		if cur.A <= last.B {
			if cur.B > last.B {
				last.B = cur.B
			}
		} else {
			merged = append(merged, cur)
		}
	}

	return merged
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var pairs []Pair
	var sol int64 = 0

	for scanner.Scan() {
		line := scanner.Text()

		if line == "" {
			break
		} else {
			bounds := strings.SplitN(line, "-", 2)

			x, _ := strconv.ParseInt(bounds[0], 10, 64)
			y, _ := strconv.ParseInt(bounds[1], 10, 64)

			pairs = append(pairs, Pair{x, y})
		}
	}

	merged := mergeIntervals(pairs)

	for _, cur := range merged {
		sol += cur.B - cur.A + 1
	}
	fmt.Println(sol)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
