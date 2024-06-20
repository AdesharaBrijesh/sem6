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
$uniqueArray = array_unique($array);
echo "Original array: " . implode(", ", $array) . "<br>";
echo "Array after removing duplicates: " . implode(", ", $uniqueArray) . "<br>";
$uniqueArray = array();
foreach ($array as $value) {
    if (!in_array($value, $uniqueArray)) {
        $uniqueArray[] = $value;
    }
}
echo "Array after removing duplicates without using in-built function: " . implode(", ", $uniqueArray);
?>
