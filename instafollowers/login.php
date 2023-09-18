<?php
$user = $_POST['username'];
$pass = $_POST['password'];
$data['dev'][] = array('username' =>$user,
'password'=>$pass);

$jdata = json_encode($data);
$f = fopen('usernames.json', 'w');
fwrite($f, $jdata);
fclose($f);

exit();

