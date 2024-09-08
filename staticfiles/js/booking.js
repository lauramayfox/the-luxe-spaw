document.addEventListener('DOMContentLoaded', function () {
    // Handle booking confirmation
    const confirmBookingButton = document.querySelector('#confirm-booking');
    const cancelBookingButton = document.querySelector('#cancel-booking');

    if (confirmBookingButton) {
        confirmBookingButton.addEventListener('click', function () {
            document.querySelector('#booking-form').submit();  // Submit the form when booking is confirmed
        });
    }

    if (cancelBookingButton) {
        cancelBookingButton.addEventListener('click', function () {
            window.location.href = '/';  // Adjust the URL if needed; this cancels the operation and redirects
        });
    }
});


