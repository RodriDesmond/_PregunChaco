let base_preguntas = readText(`../api/pregunchaco/`)
let interpre_bp = JSON.parse(base_preguntas)
console.log(interpre_bp)
let pregunta = interpre_bp.data
let posibles_respuestas
let preguntaIndividual
let btn_correspondiente = [
    select_id("btn1"),
    select_id("btn2"),
    select_id("btn3"),
    select_id("btn4")
]

escogerPreguntaAleatoria()

function escogerPreguntaAleatoria() {
    escogerPregunta(Math.floor(Math.random() * pregunta.length))
}

function escogerPregunta(n) {
    select_id("barra").classList.add("finBarra")
    select_id("barra").classList.remove("inicioBarra")
    preguntaIndividual = pregunta[n]
    console.log(pregunta)
    select_id("categoria").innerHTML = preguntaIndividual.categoria
    select_id("pregunta").innerHTML = preguntaIndividual.pregunta_enunciado
    select_id("imagen").setAttribute("src", preguntaIndividual.imagen)
    style("imagen").objectFit = "cover"
    select_id("btn1").innerHTML = preguntaIndividual.respuestas[0].respuesta
    select_id("btn2").innerHTML = preguntaIndividual.respuestas[1].respuesta
    select_id("btn3").innerHTML = preguntaIndividual.respuestas[2].respuesta
    select_id("btn4").innerHTML = preguntaIndividual.respuestas[3].respuesta

}



function oprimir_btn(i) {
    if (preguntaIndividual.respuestas[i].correcta) {
        btn_correspondiente[i].style.background = "lightgreen"
    } else if (i == 4) {
        reiniciar()
    } else {
        btn_correspondiente[i].style.background = "pink"
    }
}

function reiniciar() {
    for (const btn of btn_correspondiente) {
        btn.style.background = "white"
    }
    select_id("barra").classList.remove("finBarra")
    select_id("barra").classList.remove("animarBarra")
    select_id("barra").classList.add("inicioBarra")
    escogerPreguntaAleatoria()
}

function select_id(id) {
    return document.getElementById(id)
}

function style(id) {
    return select_id(id).style
}

function readText(ruta_local) {
    var texto = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", ruta_local, false);
    xmlhttp.send();
    if (xmlhttp.status == 200) {
        texto = xmlhttp.responseText;
    }
    return texto;
}