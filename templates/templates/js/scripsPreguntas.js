let base_preguntas = readText("base-preguntas.json")
let interpre_bp = JSON.parse(base_preguntas)
let pregunta
let posibles_respuestas
let btn_correspondiente = [
    select_id("btn1"),
    select_id("btn2"),
    select_id("btn3"),
    select_id("btn4")
]

escogerPreguntaAleatoria()

function escogerPreguntaAleatoria() {
    escogerPregunta(Math.floor(Math.random() * interpre_bp.length))
}

function escogerPregunta(n) {
    select_id("barra").classList.add("finBarra")
    select_id("barra").classList.remove("inicioBarra")
    pregunta = interpre_bp[n]
    select_id("categoria").innerHTML = pregunta.categoria
    select_id("pregunta").innerHTML = pregunta.pregunta
    select_id("imagen").setAttribute("src", pregunta.imagen)
    style("imagen").objectFit = pregunta.objectFit
    desordenarRespuestas(pregunta)

    if (pregunta.imagen) {
        style("imagen").height = "200px"
        style("imagen").width = "100%"
    } else {
        style("imagen").height = "0px"
        style("imagen").width = "0px"
    }
}

function desordenarRespuestas(pregunta) {
    posibles_respuestas = [pregunta.respuesta,
    pregunta.incorrecta1,
    pregunta.incorrecta2,
    pregunta.incorrecta3
    ]
    posibles_respuestas.sort(() => Math.random() - 0.5)
    select_id("btn1").innerHTML = posibles_respuestas[0]
    select_id("btn2").innerHTML = posibles_respuestas[1]
    select_id("btn3").innerHTML = posibles_respuestas[2]
    select_id("btn4").innerHTML = posibles_respuestas[3]
}

function oprimir_btn(i) {
    if (posibles_respuestas[i] == pregunta.respuesta) {
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