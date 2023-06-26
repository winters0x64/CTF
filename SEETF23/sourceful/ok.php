<?php
    ini_set('assert.active', 1);
    ini_set('display_errors', 1);
    ini_set('assert.warning', 1);
    ini_set('zend.assertions',1);
    ini_set('assert.callback', 'assert_callback');

    // Callback function to handle assertion failures
    function assert_callback(string $file,int $line,null $assertion,string $description ="ok"){
        echo "assertion failed on file"." ".$file."\n";
        echo "assertion failed on line"." ".$line."\n";
        echo "assertion "." ".$assertion."\n";
        echo "description"." ".$description;

    }
    assert(2 + 3 === 4,NULL);
?>