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
$searchValue = 3;
if (in_array($searchValue, $array)) {
    echo "$searchValue is found in the array. <br>";
} else {
    echo "$searchValue is not found in the array. <br>";
}
$searchValue = 3;
$found = false;
foreach ($array as $value) {
    if ($value === $searchValue) {
        $found = true;
        break;
    }
}
echo "Searching in the array without using in-built function. <br>";
if ($found) {
    echo "$searchValue is found in the array.";
} else {
    echo "$searchValue is not found in the array.";
}
?>
