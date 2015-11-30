<?php include("macaddy.php"); ?>
<?php
// show potential errors / feedback (from registration object)
if (isset($registration)) {
    if ($registration->errors) {
        foreach ($registration->errors as $error) {
            echo $error;
        }
    }
    if ($registration->messages) {
        foreach ($registration->messages as $message) {
            echo $message;
        }
    }
}


$macaddress = returnmacAddress();
?>


<!-- register form -->
<form method="post" action="register.php" name="registerform">
<input type="hidden" name="isBanned" value="YES">
    <!-- the user name input field uses a HTML5 pattern check -->
    <label for="login_input_macaddress">Mac Address</label>
    <input id="login_input_macaddress" class="login_input" type="text" pattern="[a-zA-Z0-9]{2,64}" value="<?php echo $macaddress; ?>" name="macaddress" required /> 
<br>
    <label for="login_input_username">Username (only letters and numbers, 2 to 64 characters)</label>
    <input id="login_input_username" class="login_input" type="text" pattern="[a-zA-Z0-9]{2,64}" name="user_name" required /> 
<br>
    <!-- the email input field uses a HTML5 email type check -->
    <label for="login_input_email">User's email</label>
    <input id="login_input_email" class="login_input" type="email" name="user_email" required />
<br>
    <label for="login_input_password_new">Password (min. 6 characters)</label>
    <input id="login_input_password_new" class="login_input" type="password" name="user_password_new" pattern=".{6,}" required autocomplete="off" />
<br>
    <label for="login_input_password_repeat">Repeat password</label>
    <input id="login_input_password_repeat" class="login_input" type="password" name="user_password_repeat" pattern=".{6,}" required autocomplete="off" />
<br>
    <input type="submit"  name="register" value="Register" />
</form>

<!-- backlink -->
<a href="index.php">Back to Login Page</a>
