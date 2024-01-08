package main

import (
	"fmt"
	"os"
	"strings"
)

var flag = "irisctf{this_is_not_the_real_flag}"


func main() {
	runed := []string{}
	z := rune(0)

	for _, v := range flag {
		fmt.Println("v+z :",v+z)
		runed = append(runed, string(v+z))
		fmt.Println("z :",z)
		fmt.Println("v :",v)
		fmt.Println("runed :",runed)
		z = v
	}

	flag = strings.Join(runed, "")
	fmt.Println(runed)
	fmt.Println("asdasd")
	file, err := os.OpenFile("the", os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
		fmt.Println(err)
		return
	}

	defer file.Close()
	if _, err := file.Write([]byte(flag)); err != nil {
		fmt.Println(err)
		return
	}
}
