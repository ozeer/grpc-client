<?php

require_once 'vendor/autoload.php';

use Grpc\ChannelCredentials;
use Pb\GreeterClient;
use Pb\HelloRequest;
use Pb\HelloResponse;

// 创建客户端实例
$helloClient = new GreeterClient('127.0.0.1:8972', [
    'credentials' => ChannelCredentials::createInsecure()
]);

$helloRequest = new HelloRequest();
$helloRequest->setName("Alan");
$request = $helloClient->SayHello($helloRequest)->wait();

// 返回数组
/** @var array $status */
/** @var HelloResponse $response */
list($response, $status) = $request;

print_r("Greeter client received: ". $response->getReply());

// var_dump($response->getReply());
// echo PHP_EOL;
// var_dump($status);