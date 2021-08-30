var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data() {
        return {
            categoria: "",
            puntaje: [],

        }
    },
    methods: {
        getRanking() {
            var _this = this
            fetch(`/api/pregunchaco/scoreboard`)
                .then(response => response.json())
                .then(result => {
                    console.log(result)
                    _this.puntaje = result.data
                })

        },
        filtrarYordenar: function() {
            return this.puntaje.filter(p => !p.categoria.indexOf(this.categoria)).slice().sort(function(a, b) {
                return (a.puntaje < b.puntaje) ? 1 : -1;
            });
        },
        onChange(event) {
            console.log(event.target.value)
        },
    },
    created() {
        this.getRanking()
        console.log('Pagina Cargada')
    }

});