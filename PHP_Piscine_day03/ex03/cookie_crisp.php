<?php
$name = $_GET[name];
$value = $_GET[value];
if ($_GET[action] == "set"){
    setcookie($name, $value, time() + (86400 * 30));
}
if ($_GET[action] == "get"){
    if ($_COOKIE[$name] != FALSE){
        echo $_COOKIE[$name];
    }
}
if ($_GET[action] == "del"){
	setcookie($name, $value, time() - 3600);
}
?>