var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data() {
        return {
            categoria: document.getElementById("categoria").value,
            preguntas: [],
            soluciones: [],
        }
    },
    methods: {
        enviarResultado() {
            console.log(this.soluciones)
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
                var radios = document.querySelectorAll(`#radio-${id}`)
                for (var i = 0; i < respuestas.length; i++) {
                    if (respuestas[i].respuesta == event.target.value) {
                        solucion = {
                            'pregunta_id': id,
                            'respuesta': respuestas[i].respuesta
                        }
                        this.soluciones.push(solucion)
                        for (var j = 0; j < respuestas.length; j++) {
                            radios[j].disabled = true
                        }
                        if (respuestas[i].correcta) {
                            element.classList = "text-success mt-3"
                            element.innerHTML = "Correcto 🤩"
                        } else {
                            element.classList = "text-danger mt-3"
                            element.innerHTML = "Incorrecto 😵"
                        }
                    }
                }
            })
        }
    },

    created() {
        this.getPreguntas()
        console.log('Pagina Cargada')
    },
});