package main

import "net/http"

func handle(w http.ResponseWriter, r *http.Request){
	w.Write([]byte("welcome!"))
}

func main(){
	http.HandleFunc("/", handle)
	http.ListenAndServe(":8001", nil)
}
