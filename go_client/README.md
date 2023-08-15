##### 生成Go版本gRPC代码
```
protoc --go_out=. hello.proto
protoc --go-grpc_out=. hello.proto
```