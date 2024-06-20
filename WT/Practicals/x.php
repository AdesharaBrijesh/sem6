<?php 
$x = 20;
$y = 30;
function fun(){
    $y = $GLOBAL['$x'] + $GLOBAL['$y'];
}
fun();
echo $y;
?>