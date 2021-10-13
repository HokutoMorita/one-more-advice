package main

import (
	"fmt"
	"one_more_advice_api/src/app/infrastructure"
)

func main() {
	fmt.Println("サーバ起動")
	infrastructure.Init()
}

