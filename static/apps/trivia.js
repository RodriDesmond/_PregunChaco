var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data() {
        return {
            categoria: document.getElementById("categoria").value,
            preguntas: [],
        }
    },
    methods: {
        getPreguntas() {
            var _this = this
            fetch(`/api/pregunchaco/?categoria=${this.categoria}`)
                .then(response => response.json())
                .then(result => {
                    console.log(result)
                    _this.preguntas = result.data
                })
        },
        checkRespuesta(event) {
            this.preguntas.map(pregunta => {
                respuestas = pregunta.respuestas
                id = pregunta.id
                var element = document.getElementById(`mensaje_respuesta-${id}`)
                for (var i = 0; i < respuestas.length; i++) {
                    if (respuestas[i].respuesta == event.target.value)
                        if (respuestas[i].correcta) {
                            console.log('Correcto: ')
                            element.classList = "text-success mt-3"
                            element.innerHTML = "Correcto 🤩"
                        } else {
                            console.log('INCORRECTO: ')
                            element.classList = "text-danger mt-3"
                            element.innerHTML = "Incorrecto 😵"
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