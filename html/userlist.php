<?php
require_once("config/db.php");

//connection to the database
$dbhandle = mysql_connect($DB_HOST, $DB_NAME, $DB_PASS) 
 or die("Unable to connect to MySQL");
echo "Connected to MySQL<br>";

//select a database to work with
$selected = mysql_select_db("examples",$dbhandle) 
  or die("Could not select examples");

//execute the SQL query and return records
$result = mysql_query("SELECT user_name, isBanned FROM users");

//fetch tha data from the database 
while ($row = mysql_fetch_array($result)) {
   echo "UserName:".$row{'user_name'}." Banned:".$row{'isBanned'}."<br>";
}
//close the connection
mysql_close($dbhandle);
?>