// Function to update booking modal with selected details
    function updateBookingModal() {
        document.getElementById('booking-service').textContent = document.getElementById('id_service').selectedOptions[0].text;
        document.getElementById('booking-groomer').textContent = document.getElementById('id_groomer').selectedOptions[0].text;
        document.getElementById('booking-date').textContent = document.getElementById('id_booking_date').value;
        document.getElementById('booking-time').textContent = document.getElementById('id_booking_time').selectedOptions[0].text;
    }

    // Handle booking confirmation
    const confirmBookingButton = document.getElementById('confirm-booking');
    if (confirmBookingButton) {
        confirmBookingButton.addEventListener('click', function () {
            console.log('Confirm booking button clicked');
            // Submit the form or make AJAX request to confirm booking
            document.getElementById('booking-form').submit();
        });
    }

    // Handle the cancel booking action
    const cancelBookingButton = document.getElementById('cancel-booking');
    if (cancelBookingButton) {
        cancelBookingButton.addEventListener('click', function () {
            window.location.href = '/'; // Redirect to home
        });
    }

    // Show booking confirmation modal with details
    const bookButton = document.querySelector('[data-bs-target="#confirmBookingModal"]');
    if (bookButton) {
        bookButton.addEventListener('click', function () {
            updateBookingModal();
        });
    }







