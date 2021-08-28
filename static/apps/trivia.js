var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data() {
        return {
            categoria: document.getElementById("categoria").value,
            preguntas: [],
            soluciones: [],
            curiosidad: false,
        }
    },
    methods: {
        enviarResultado() {
            fetch('/api/pregunchaco/puntos', {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        data: JSON.stringify(this.soluciones)
                    })
                })
                .then(res => res.json())
                .then(result => {
                    console.log(result)
                })
        },
        getPreguntas() {
            var _this = this
            fetch(`/api/pregunchaco/?categoria=${this.categoria}`)
                .then(response => response.json())
                .then(result => {
                    console.log(result)
                    _this.preguntas = result.data
                })
        },
        checkRespuesta(event, resultado_index, id) {
            this.preguntas.map(pregunta => {
                respuestas = pregunta.respuestas
                id = pregunta.id
                var element = document.getElementById(`mensaje_respuesta-${id}`)
                var dato = document.getElementById(`dato-${id}`)
                var radios = document.querySelectorAll(`#radio-${id}`)
                for (var i = 0; i < respuestas.length; i++) {
                    if (respuestas[i].respuesta == event.target.value) {
                        for (var j = 0; j < respuestas.length; j++) {
                            radios[j].disabled = true
                        }
                        if (respuestas[i].correcta) {
                            element.classList = "text-success mt-3"
                            element.innerHTML = "Correcto 🤩"
                            dato.innerHTML = `<strong><em>${[[pregunta.dato]]}</em></strong >`
                            correcto = true
                        } else {
                            element.classList = "text-danger mt-3"
                            element.innerHTML = "Incorrecto 😵"
                            dato.innerHTML = `<strong><em>${[[pregunta.dato]]}</em></strong >`
                            correcto = false
                        }
                        solucion = {
                            'categoria': pregunta.categoria,
                            'pregunta_id': id,
                            'correcto': correcto,
                            'respuesta': respuestas[i].respuesta
                        }
                        this.soluciones.push(solucion)
                    }
                }
            })
        }
    },
    mounted() {
        this.getPreguntas()
        console.log('Pagina Cargada')
    },
});