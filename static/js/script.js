/*
 * script.js — a small JavaScript file that adds interactivity to the form.
 *
 * This script runs a live character counter on the "Your name" input field.
 * Every time the user types a character, the counter updates instantly —
 * without needing to send anything to the server.
 */

// Wait until the browser has fully loaded the HTML before running this code
document.addEventListener("DOMContentLoaded", function () {

    // Find the name input field and the <small> element we update
    const nameInput = document.getElementById("student_name");
    const counter   = document.getElementById("name_counter");

    // Listen for the "input" event — fired every time the user types or deletes
    nameInput.addEventListener("input", function () {
        const length = nameInput.value.length;

        // Update the counter text below the input
        if (length === 0) {
            counter.textContent = "";
        } else {
            counter.textContent = length + " / 50 characters";
        }
    });

});
