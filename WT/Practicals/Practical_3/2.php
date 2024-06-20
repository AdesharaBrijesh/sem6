<?php
echo "Adeshara Brijesh_21012021001 <br>";
$array=[];
$n=10;
echo "Array is: ";
for($i=0;$i<$n;$i++){
    if($i%10==0) echo "<br>";
    $array[$i]=rand(-100,100);
    echo $array[$i].",";
}
echo "<br><br>";
$reversedArray = array_reverse($array);
echo "Original array: " . implode(", ", $array) . "<br>";
echo "Reversed array: " . implode(", ", $reversedArray) . "<br>";
$reversedArray = array();
$length = count($array);
for ($i = $length - 1; $i >= 0; $i--) {
    $reversedArray[] = $array[$i];
}
echo "Original array without in-built function: " . implode(", ", $array) . "<br>";
echo "Reversed array without in-built function: " . implode(", ", $reversedArray);
?>
