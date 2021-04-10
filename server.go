package main;

import (
	"net/http";
	"fmt";
)

func handle(w http.ResponseWriter, r *http.Request){
	http.ServeFile(w,r,"index.html")
}

func main(){
	fmt.Println("TeddyMark is ready to go on http://localhost:8080")
	http.HandleFunc("/", handle);
	http.ListenAndServe(":8080", nil);
}