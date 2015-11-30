<?php

// include the configs / constants for the database connection
require_once("config/db.php");


$query = "SELECT * FROM users"; //You don't need a ; like you do in SQL
$result = mysql_query($query);

echo "<table>"; // start a table tag in the HTML

while($row = mysql_fetch_array($result)){   //Creates a loop to loop through results
echo "<tr><td>" . $row['user_name'] . "</td><td>" . $row['isBanned'] . "</td></tr>";  //$row['index'] the index here is a field name
}

echo "</table>"; //Close the table in HTML

// mysql_close(); //Make sure to close out the database connection