<?php

const SESSION = 'elephant_user';
$flag = file_get_contents('/flag');


class User {
    public $name;
    private $token;

    function __construct($name) {
        $this->name = $name;
        $this->token = md5($_SERVER['REMOTE_ADDR'] . rand());
    }

    function canReadFlag() {
        return strcmp($flag, $this->token) == 0;
    }
}

if (isset($_GET['logout'])) {
    header('Location: /');
    setcookie(SESSION, NULL, 0);
    exit;
}


$user = NULL;

if ($name = $_POST['name']) {
    $user = new User($name);
    header('Location: /');
    setcookie(SESSION, base64_encode(serialize($user)), time() + 600);
    exit;
} else if ($data = @$_COOKIE[SESSION]) {
    $user = unserialize(base64_decode($data));
}



?><!DOCTYPE html>
<head>
    <title>Elephant</title>
    <meta charset='utf-8'>
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head>
<body>
    <?php if (!$user): ?>
        <div id="login">
            <h3 class="text-center text-white pt-5">Are you familiar with PHP?</h3>
            <div class="container">
                <div id="login-row" class="row justify-content-center align-items-center">
                    <div id="login-column" class="col-md-6">
                        <div id="login-box" class="col-md-12">
                            <form id="login-form" class="form" action="" method="post">
                                <h3 class="text-center text-info">What's your name!?</h3>
                                <div class="form-group">
                                    <label for="name" class="text-info">Name:</label><br>
                                    <input type="text" name="name" id="name" class="form-control">
                                </div>
                                <div class="form-group">
                                    <input type="submit" name="submit" class="btn btn-info btn-md" value="let me in">
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    <?php else: ?>
        <h3 class="text-center text-white pt-5">You may want to read the source code.</h3>
        <div class="container" style="text-align: center">
            <img src="images/elephant2.png">
        </div>
        <hr>
        <div class="container">
            <div class="row justify-content-center align-items-center">
                <div class="col-md-6">
                    <div class="col-md-12">
                        <h3 class="text-center text-info">Do you know?</h3>
                        <h3 class="text-center text-info">PHP's mascot is an elephant!</h3>
                        Hello, <b><?= $user->name ?></b>!
                        <?php if ($user->canReadFlag()): ?>
                            This is your flag: <b><?= $flag ?></b>
                        <?php else: ?>
                            Your token is not sufficient to read the flag!
                        <?php endif; ?>
                        <a href="?logout">Logout!</a>
                    </div>
                </div>
            </div>
        </div>
    <?php endif ?>
</body>
