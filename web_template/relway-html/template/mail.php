<?php
// declare our variables
$name = $_POST['name'];
$email = $_POST['email'];
$message = nl2br($_POST['message']);

// set a title for the message
$subject = "Message from Your Website";
$body = "From $name, \n\n$message";
$headers = 'From: '.$email.'' . "\r\n" .
    'Reply-To: '.$email.'' . "\r\n" .
	'Content-type: text/html; charset=utf-8' . "\r\n" .
    'X-Mailer: PHP/' . phpversion();

// put your email address here
mail("zoomarts.com@gmail.com", $subject, $body, $headers);
?>

<!--Display a Thank you message in the callback -->
<div class="mail_response">
    <h4>Thank you <?php echo $name ?>!</h4>
    <p>We'll be in touch real soon!</p>
</div>    