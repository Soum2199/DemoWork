<?php

$message = "Try programiz.pro"; 
// $lengthy = strlen($message);
echo $message;
// echo PHP_EOL.$lengthy;
echo PHP_EOL.strlen($message);

$a = [1,2,3,4];
echo  PHP_EOL;
print_r($a);
echo PHP_EOL . implode(', ', $a);

?>

-----------------------------------------------------------------------------------------------------------------------------------------

<?php

echo "Try programiz.pro" . PHP_EOL . PHP_EOL;

// $hi = true;
// $hey = !0;
$hi = TRUE;
// echo "The sentence written is " . var_dump($hi) . PHP_EOL;
echo "The sentence written is " . var_export($hi, true) . PHP_EOL;
// echo "The sentence written is " . boolToString($hi) . PHP_EOL;
// echo "The sentence written is " . (bool)$hi . PHP_EOL;
echo "The sentence written is " . ($hi ? 'true' : 'false') . PHP_EOL;
// echo "The sentence written is " . (!($hi) ? 'true' : 'false') . PHP_EOL;

?>
--------------------------------------------------------------------------------------------------------------------------------------------
<?php

echo "Try programiz.pro" . PHP_EOL . PHP_EOL;

// $hi = true;
// $hey = !0;
$hi = TRUE;
// echo "The sentence written is " . var_dump($hi) . PHP_EOL;
echo "The sentence written is " . var_export($hi, true) . PHP_EOL;
// echo "The sentence written is " . boolToString($hi) . PHP_EOL;
// echo "The sentence written is " . (bool)$hi . PHP_EOL;
echo "The sentence written is " . ($hi ? 'true' : 'false') . PHP_EOL;
// echo "The sentence written is " . (!($hi) ? 'true' : 'false') . PHP_EOL;

$c = "solving from";
echo "Try " . $c . " programiz.pro";
echo PHP_EOL . $c.length;  // wrogn approach
echo PHP_EOL . strlen($c);  // correct approach
?>
-----------------------------------------------------------------------------------------------------------------------------------------------
<?php
$n = 8;
for($i = 1; $i<=$n; $i++){
    if( $i == 6){
        // break;
        continue;
    }
    echo "This is our attempt no. " . $i . ", ok." . PHP_EOL;
}
// echo "The number is: ". ($n+1) . PHP_EOL . "Thank you.";
?>

<!--for($j of $n)-->
