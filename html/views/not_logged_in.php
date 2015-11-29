<?php
// show potential errors / feedback (from login object)
if (isset($login)) {
    if ($login->errors) {
        foreach ($login->errors as $error) {
            echo $error;
        }
    }
    if ($login->messages) {
        foreach ($login->messages as $message) {
            echo $message;
        }
    }
}
?>

<?php 
function returnmacAddress() {
// This code is under the GNU Public Licence
// Written by michael_stankiewicz {don't spam} at yahoo {no spam} dot com 
// Get the arp executable path
$location = `which arp`;
$location = rtrim($location);

// Execute the arp command and store the output in $arpTable
$arpTable = `$location -a`;

// Split the output so every line is an entry of the $arpSplitted array
$arpSplitted = split("\n",$arpTable);

// Get the remote ip address (the ip address of the client, the browser)
$remoteIp = $GLOBALS['REMOTE_ADDR'];
$remoteIp = str_replace(".", "\\.", $remoteIp);

// Cycle the array to find the match with the remote ip address
foreach ($arpSplitted as $value) {
	// Split every arp line, this is done in case the format of the arp
	// command output is a bit different than expected
	$valueSplitted = split(" ",$value);
	foreach ($valueSplitted as $spLine) {
		if (preg_match("/$remoteIp/",$spLine)) {
		$ipFound = true;
		}
		// The ip address has been found, now rescan all the string
		// to get the mac address
		if ($ipFound) {
			// Rescan all the string, in case the mac address, in the string
			// returned by arp, comes before the ip address
			// (you know, Murphy's laws)
			reset($valueSplitted);
			foreach ($valueSplitted as $spLine) {
				if (preg_match("/[0-9a-f][0-9a-f][:-]"."[0-9a-f][0-9a-f][:-]"."[0-9a-f][0-9a-f][:-]"."[0-9a-f][0-9a-f][:-]"."[0-9a-f][0-9a-f][:-]"."[0-9a-f][0-9a-f]/i",$spLine)) {
					return $spLine;
				}
			}
		}
		$ipFound = false;
	}
}
return false;
}
?>
<br>
<b>Your Mac Address: </b>
<?php echo returnmacAddress(); ?> <br><br>


<!-- login form box -->
<form method="post" action="index.php" name="loginform">

    <label for="login_input_username">Username</label>
    <input id="login_input_username" class="login_input" type="text" name="user_name" required />
<br>
    <label for="login_input_password">Password</label>
    <input id="login_input_password" class="login_input" type="password" name="user_password" autocomplete="off" required />

    <input type="submit"  name="login" value="Log in" />

</form>

<a href="register.php">Register new account</a>
