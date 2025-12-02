package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func powInt(base int64, exp int) int64 {
	result := int64(1)
	b := base
	e := exp

	for e > 0 {
		if e%2 == 1 {
			result *= b
		}
		b *= b
		e /= 2
	}

	return result
}

func digitCount(num int64) int {
	if num < 0 {
		num = -num
	}

	return len(strconv.FormatInt(num, 10))
}

func repeatFactor(baseDigits, repeatCount int) int64 {
	totalDigits := baseDigits * repeatCount
	numerator := powInt(10, totalDigits) - 1
	denominator := powInt(10, baseDigits) - 1
	return numerator / denominator
}

func isPrimitive(num int64, digits int) bool {
	if digits <= 1 {
		return true
	}

	s := strconv.FormatInt(num, 10)
	if len(s) < digits {
		s = strings.Repeat("0", digits-len(s)) + s
	}

	for length := 1; length <= digits/2; length++ {
		if digits%length != 0 {
			continue
		}

		match := true
		for i := length; i < digits; i++ {
			if s[i] != s[i%length] {
				match = false
				break
			}
		}

		if match {
			return false
		}
	}

	return true
}

func solve(x int64, y int64) int64 {
	if x > y {
		return 0
	}

	total := int64(0)
	maxDigits := digitCount(y)

	for baseDigits := 1; baseDigits <= maxDigits; baseDigits++ {
		baseMin := powInt(10, baseDigits-1)
		if baseDigits == 1 {
			baseMin = 1
		}
		baseMax := powInt(10, baseDigits) - 1

		cache := make(map[int64]bool)

		for repeatCount := 2; baseDigits*repeatCount <= maxDigits; repeatCount++ {
			factor := repeatFactor(baseDigits, repeatCount)

			low := (x + factor - 1) / factor
			high := y / factor

			if low < baseMin {
				low = baseMin
			}
			if high > baseMax {
				high = baseMax
			}

			for base := low; base <= high; base++ {
				if baseDigits > 1 {
					val, ok := cache[base]
					if !ok {
						val = isPrimitive(base, baseDigits)
						cache[base] = val
					}
					if !val {
						continue
					}
				}

				total += base * factor
			}
		}
	}

	return total
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	solution := int64(0)

	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())

		chunks := strings.Split(line, ",")
		for _, chunk := range chunks {
			chunk = strings.TrimSpace(chunk)
			if chunk == "" {
				continue
			}

			bounds := strings.SplitN(chunk, "-", 2)
			if len(bounds) != 2 {
				log.Fatalf("invalid pair %q", chunk)
			}

			x, err := strconv.ParseInt(bounds[0], 10, 64)
			if err != nil {
				log.Fatalf("invalid x value %q: %v", bounds[0], err)
			}

			y, err := strconv.ParseInt(bounds[1], 10, 64)
			if err != nil {
				log.Fatalf("invalid y value %q: %v", bounds[1], err)
			}

			solution += solve(x, y)
		}
	}

	fmt.Println(solution)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
