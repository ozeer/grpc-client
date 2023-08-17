<?php
// GENERATED CODE -- DO NOT EDIT!

// Original file comments:
// 版本声明，使用Protocol Buffers v3版本
namespace Client;

/**
 * 定义服务
 */
class GreeterClient extends \Grpc\BaseStub {

    /**
     * @param string $hostname hostname
     * @param array $opts channel options
     * @param \Grpc\Channel $channel (optional) re-use channel object
     */
    public function __construct($hostname, $opts, $channel = null) {
        parent::__construct($hostname, $opts, $channel);
    }

    /**
     * SayHello 方法
     * @param \Client\HelloRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     * @return \Grpc\UnaryCall
     */
    public function SayHello(\Client\HelloRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/pb.Greeter/SayHello',
        $argument,
        ['\Client\HelloResponse', 'decode'],
        $metadata, $options);
    }

}
