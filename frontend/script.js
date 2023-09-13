document.addEventListener("DOMContentLoaded", function () {
    const alumnoForm = document.getElementById("alumno-form");
    const alumnoList = document.getElementById("alumno-list");
    const alumnos = [];
    let modoEdicion = false;
    let legajoEdicion = null;
    
    const legajosUtilizados = new Set(); // Agrega esta línea para definir el conjunto de legajos utilizados

    function generarLegajoUnico() {
        let legajo;
        do {
            legajo = Math.floor(Math.random() * 2000) + 1;
        } while (legajosUtilizados.has(legajo));

        legajosUtilizados.add(legajo);
        return legajo;
    }

    function agregarAlumno(nombre, apellido, edad) {
        const nuevoAlumno = {
            legajo: generarLegajoUnico(),
            nombre: nombre,
            apellido: apellido,
            edad: edad
        };
        alumnos.push(nuevoAlumno);
        mostrarAlumnos();
    }

    function mostrarAlumnos() {
        alumnoList.innerHTML = "";

        alumnos.forEach(function (alumno) {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${alumno.legajo}</td>
                <td>${alumno.nombre}</td>
                <td>${alumno.apellido}</td>
                <td>${alumno.edad}</td>
                <td>
                    <button class="btn-editar" data-legajo="${alumno.legajo}">Editar</button>
                    <button class="btn-eliminar" data-legajo="${alumno.legajo}">Eliminar</button>
                </td>
            `;
            alumnoList.appendChild(row);
        });
    }

    alumnoForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const nombre = document.getElementById("nombre").value;
        const apellido = document.getElementById("apellido").value;
        const edad = document.getElementById("edad").value;

        if (modoEdicion) {
            actualizarAlumno(legajoEdicion, nombre, apellido, edad);
        } else {
            agregarAlumno(nombre, apellido, edad);
        }

        alumnoForm.reset();
        modoEdicion = false;
        legajoEdicion = null;
        document.getElementById("guardar").textContent = "Guardar";
    });

    alumnoList.addEventListener("click", function (event) {
        const target = event.target;
        if (target.classList.contains("btn-editar")) {
            const legajo = parseInt(target.getAttribute("data-legajo"));
            editarAlumno(legajo);
        } else if (target.classList.contains("btn-eliminar")) {
            const legajo = parseInt(target.getAttribute("data-legajo"));
            eliminarAlumno(legajo);
        }
    });

    function editarAlumno(legajo) {
        const alumno = alumnos.find(alumno => alumno.legajo === legajo);

        if (!alumno) {
            alert("Alumno no encontrado");
            return;
        }

        document.getElementById("alumno-legajo").value = alumno.legajo;
        document.getElementById("nombre").value = alumno.nombre;
        document.getElementById("apellido").value = alumno.apellido;
        document.getElementById("edad").value = alumno.edad;

        document.getElementById("guardar").textContent = "Actualizar";
        modoEdicion = true;
        legajoEdicion = legajo;
    }

    function actualizarAlumno(legajo, nombre, apellido, edad) {
        const alumnoIndex = alumnos.findIndex(alumno => alumno.legajo === legajo);

        if (alumnoIndex === -1) {
            alert("Alumno no encontrado");
            return;
        }

        alumnos[alumnoIndex].nombre = nombre;
        alumnos[alumnoIndex].apellido = apellido;
        alumnos[alumnoIndex].edad = edad;

        mostrarAlumnos();
    }

    function eliminarAlumno(legajo) {
        const confirmacion = confirm("¿Estás seguro de que deseas eliminar a este alumno?");

        if (confirmacion) {
            const alumnoIndex = alumnos.findIndex(alumno => alumno.legajo === legajo);

            if (alumnoIndex === -1) {
                alert("Alumno no encontrado");
                return;
            }

            alumnos.splice(alumnoIndex, 1);
            mostrarAlumnos();
        }
    }
});

