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
sort($array);
echo "Sorted array: " . implode(", ", $array) . "<br>";
$length = count($array);
for ($i = 0; $i < $length - 1; $i++) {
    for ($j = 0; $j < $length - $i - 1; $j++) {
        if ($array[$j] > $array[$j + 1]) {
            $temp = $array[$j];
            $array[$j] = $array[$j + 1];
            $array[$j + 1] = $temp;
        }
    }
}
echo "Sorted array without using in-built function: " . implode(", ", $array);
?>
