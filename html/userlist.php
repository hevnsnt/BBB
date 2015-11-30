<?php
$username = "root";
$password = "password";
$hostname = "localhost"; 

//connection to the database
$dbhandle = mysql_connect($hostname, $username, $password) 
 or die("Unable to connect to MySQL");
//echo "Connected to MySQL<br>";

//select a database to work with
$selected = mysql_select_db("seckc",$dbhandle); 
//  or die("Could not select seckc");

//execute the SQL query and return records
$result = mysql_query("SELECT user_name, isBanned FROM users");

echo "Player List"
//fetch tha data from the database 
while ($row = mysql_fetch_array($result)) {
   echo "User ID:".$row{'user_name'}." Banned:".$row{'isBanned'}."<br>";
}
//close the connection
mysql_close($dbhandle);
?>
