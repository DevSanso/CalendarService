package args

import (
	"encoding/json"
	"io/ioutil"
)

type BasicServiceArgs struct {
	DB struct {
		User   string `json:user`
		Passwd string `json:passwd`
		Host   string `json:host`
		Port   int    `json:port`
		Dbname string `json:dbname`
	} `json:db`
	Server struct {
		Host string `json:host`
		Port int    `json:port`
	} `json:server`
}

func ParsingConfigWithFile[T any](path string) (*T, error) {
	data, err := ioutil.ReadFile(path)
	if err != nil {
		return nil, err
	}
	var obj *T = new(T)
	return obj, json.Unmarshal(data, obj)
}
func ParsingConfigString[T any](s string) (*T, error) {
	var obj *T = new(T)
	return obj, json.Unmarshal([]byte(s), obj)
}
