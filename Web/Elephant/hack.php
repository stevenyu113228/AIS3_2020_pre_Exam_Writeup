<?php

class User{
    public $name;
    public $token;
}
$test = new User();
$test->name = "123456";
$test->token = array("8","7","8","7");

echo serialize($test);
//O:4:"User":2:{s:4:"name";s:6:"123456";s:5:"token";a:4:{i:0;s:1:"8";i:1;s:1:"7";i:2;s:1:"8";i:3;s:1:"7";}}