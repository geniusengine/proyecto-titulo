// Mostrar y ocultar el menú lateral
function toggleMenu() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('active');
}

// Confirmar notificación
function confirmarNotificacion(form) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: "Se notificará esta causa.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, notificar'
    }).then((result) => {
        if (result.isConfirmed) {
            form.submit();
        }
    });
}

// Confirmar estampado
function confirmarEstampado(form) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: "Se estampará esta causa.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, estampar'
    }).then((result) => {
        if (result.isConfirmed) {
            form.submit();
        }
    });
}

// Buscar demandas
function buscarDemanda() {
    const input = document.getElementById('buscador');
    const filter = input.value.toLowerCase();
    const table = document.getElementById('tablaDemandas');
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName('td');
        let match = false;

        for (let j = 0; j < cells.length; j++) {
            const cell = cells[j];
            if (cell && cell.textContent.toLowerCase().includes(filter)) {
                match = true;
                break;
            }
        }
        rows[i].style.display = match ? '' : 'none';
    }
}
