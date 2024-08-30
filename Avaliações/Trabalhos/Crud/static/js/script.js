document.addEventListener('DOMContentLoaded', function () {
    const reservaForm = document.querySelector('form');

    if (reservaForm) {
        reservaForm.addEventListener('submit', function (event) {
            let checkin = new Date(document.querySelector('[name="data_checkin"]').value);
            let checkout = new Date(document.querySelector('[name="data_checkout"]').value);
            if (checkout <= checkin) {
                alert('Data de check-out deve ser posterior à data de check-in');
                event.preventDefault();
            }
        });
    }
});
