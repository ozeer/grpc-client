###
1、安装插件
https://learnku.com/articles/48738

2、生成php的gRPC代码
protoc --php_out=./ --grpc_out=./ --plugin=protoc-gen-grpc=/usr/local/bin/grpc_php_plugin hello.proto

3、参考文档
- https://juejin.cn/post/7143433324457902116
- https://learnku.com/articles/48738
- https://learnku.com/articles/36277