<?php
    // Check for a false value of a letter that is not
    // in your own name and print out an error message
	NaN
    $myName="Larry";
    $search="e";
    
    if(strpos($myName,$search) == false){
        echo "Sorry, no in 'Larry'";
    }
    else{
        echo "Fine, is in 'Larry'";
    }
    
    $words = array("Hi","Well","Bye");
    
    foreach($words as $iterator):
        echo "<p> $iterator </p>";    
    endforeach;

?>
