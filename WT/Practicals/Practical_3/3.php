<?php
$array1=[];
$n=10;
echo "Array1 is: ";
for($i=0;$i<$n;$i++){
    if($i%10==0) echo "<br>";
    $array1[$i]=rand(-100,100);
    echo $array1[$i].",";
}
$array2=[];
$n=10;
echo "<br>Array2 is: ";
for($i=0;$i<$n;$i++){
    if($i%10==0) echo "<br>";
    $array2[$i]=rand(-100,100);
    echo $array2[$i].",";
}

echo "<br><br>";
$mergedArray = array_merge($array1, $array2);
echo "Merged array: " . implode(", ", $mergedArray) . "<br>";
$mergedArray = array();
foreach ($array1 as $value) {
    $mergedArray[] = $value;
}
foreach ($array2 as $value) {
    $mergedArray[] = $value;
}
echo "Merged array without using in-built function: " . implode(", ", $mergedArray);
?>
