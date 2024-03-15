<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect post data
    $name = strip_tags(trim($_POST["name"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $subject = strip_tags(trim($_POST["subject"]));
    $message = trim($_POST["message"]);

    // Specify your email and subject
    $to = "info@makeaccessible.ai"; // CHANGE THIS to your actual email address
    $email_subject = "New submission from: $name, Subject: $subject";

    // Prepare the email body
    $email_body = "You have received a new message from the contact form on your website.\n\n";
    $email_body .= "Name: $name\n";
    $email_body .= "Email: $email\n";
    $email_body .= "Subject: $subject\n";
    $email_body .= "Message:\n$message\n";

    // Headers
    $headers = "From: $email\n";
    $headers .= "Reply-To: $email";

    // Send the email
    mail($to, $email_subject, $email_body, $headers);

    // Redirect to a thank-you page or back to the form
    header("Location: thank-you.html"); // Adjust the location as needed
} else {
    // Not a POST request, redirect back to the form or home page
    header("Location: /"); // Adjust as needed
}
?>
