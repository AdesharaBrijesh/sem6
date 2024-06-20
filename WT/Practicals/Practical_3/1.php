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
$max = max($array);
$min = min($array);

echo "Maximum number: $max<br>";
echo "Minimum number: $min<br>";
$max = $array[0];
$min = $array[0];

foreach ($array as $value) {
    if ($value > $max) {
        $max = $value;
    }
    if ($value < $min) {
        $min = $value;
    }
}
echo "Maximum number without in-built function: $max<br>";
echo "Minimum number without in-built function: $min";
?>
