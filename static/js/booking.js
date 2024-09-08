document.addEventListener('DOMContentLoaded', function () {
    console.log('booking.js is loaded'); // Debugging

    // Handle booking confirmation
    const confirmBookingButton = document.getElementById('confirm-booking');
    const cancelBookingButton = document.getElementById('cancel-booking');

    if (confirmBookingButton) {
        confirmBookingButton.addEventListener('click', function () {
            console.log('Confirm booking button clicked'); // Debugging
            document.getElementById('booking-form').submit(); // Submit the form
        });
    }

    if (cancelBookingButton) {
        cancelBookingButton.addEventListener('click', function () {
            console.log('Cancel booking button clicked'); // Debugging
            window.location.href = '/'; // Redirect or handle cancellation
        });
    }
});



