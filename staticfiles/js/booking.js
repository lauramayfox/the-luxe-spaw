
document.addEventListener('DOMContentLoaded', function () {
    // Manually initialize Bootstrap modals
    var confirmBookingModalElement = document.getElementById('confirmBookingModal');
    var confirmCancelModalElement = document.getElementById('confirmCancelModal');

    // Initialize Bootstrap Modal instances if the modal elements are found
    if (confirmBookingModalElement && confirmCancelModalElement) {
        var confirmBookingModal = new bootstrap.Modal(confirmBookingModalElement);
        var confirmCancelModal = new bootstrap.Modal(confirmCancelModalElement);

        // Get the buttons that perform actions inside the modal
        const confirmBookingButton = document.getElementById('confirm-booking');
        const cancelBookingButton = document.getElementById('cancel-booking');

        // Handle the booking confirmation action
        if (confirmBookingButton) {
            confirmBookingButton.addEventListener('click', function () {
                // Submit the form to confirm booking
                document.getElementById('booking-form').submit();
            });
        }

        // Handle the cancel booking action
        if (cancelBookingButton) {
            cancelBookingButton.addEventListener('click', function () {
                // Redirect to the create_booking page or any desired action
                window.location.href = 'create_booking.html';
            });
        }
    }
});




