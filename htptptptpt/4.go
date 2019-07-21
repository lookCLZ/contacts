package main

import (
	"net"
	"fmt"
	// "os"
)

func main() {
	conn,_:=net.Dial("tcp","127.0.0.1:8000")
	defer conn.Close()

	httpRequest:="GET /itcast88 HTTP/1.1\r\nHost:127.0.0.1:8000\r\n\r\n"

	conn.Write([]byte(httpRequest))
	
	buf:=make([]byte,4096)
	n,_:=conn.Read(buf)
	fmt.Printf("|%s|\n",string(buf[:n]))

}