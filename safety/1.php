<?
while(1){
    $pid=80;
    @unlink('a.php');
    exec('kill -9 $pid')
}
php?>