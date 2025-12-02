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

func convNum(num int64) int64 {
	digits := digitCount(num)
	pow := powInt(10, digits)
	return num*pow + num
}

func upperCandidate(y int64) int64 {
	if y < 0 {
		return -1
	}

	digits := digitCount(y)
	maxDigits := (digits + 1) / 2
	if maxDigits > 9 {
		maxDigits = 9
	}

	return powInt(10, maxDigits) - 1
}

func lowerBound(target, hi int64) int64 {
	lo := int64(0)
	result := int64(-1)

	for lo <= hi {
		mid := lo + (hi-lo)/2
		val := convNum(mid)

		if val >= target {
			result = mid
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}

	return result
}

func upperBound(target, hi int64) int64 {
	lo := int64(0)
	result := int64(-1)

	for lo <= hi {
		mid := lo + (hi-lo)/2
		val := convNum(mid)

		if val <= target {
			result = mid
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}

	return result
}

func solve(x int64, y int64) int64 {
	if x > y || y < 0 {
		return 0
	}

	hi := upperCandidate(y)
	if hi < 0 {
		return 0
	}

	first := lowerBound(x, hi)
	if first == -1 {
		return 0
	}

	firstVal := convNum(first)
	if firstVal < x || firstVal > y {
		return 0
	}

	last := upperBound(y, hi)
	if last == -1 || last < first {
		return 0
	}

	total := int64(0)
	start := first

	for start <= last {
		digits := digitCount(start)
		maxForDigits := powInt(10, digits) - 1
		end := last
		if maxForDigits < end {
			end = maxForDigits
		}

		count := end - start + 1
		sumNums := start + end

		if count%2 == 0 {
			count /= 2
		} else {
			sumNums /= 2
		}

		sumNums *= count
		factor := powInt(10, digits) + 1

		total += factor * sumNums
		start = end + 1
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
