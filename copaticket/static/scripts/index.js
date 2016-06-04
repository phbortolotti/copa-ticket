var index = {

    init: function() {
        this.ranking();
    },

    ranking: function() {
        $.ajax({
            type: "GET",
            contentType: "application/json",
            cache: false,
            url: "/api/times",
            success: function(times) {
                for (var i=0; i < times.length; i++) {
                    var escudo = times[i].url_escudo_svg,
                        nomeTime = times[i].nome,
                        nomeCartola = times[i].nome_cartola,
                        pontos = parseFloat(times[i].pontos.campeonato).toFixed(2),
                        posicao = i + 1;

                    var rowTemplate = "<tr> \
                        <td class='col-escudo'><img alt='" + nomeTime + "' src='" + escudo + "'></td> \
                        <td class='col-time text-left'><h3>" + nomeTime + "</h3><h5>" + nomeCartola + "</h5></td> \
                        <td class='col-pontos text-left'><h1><b>" + pontos + "</b> pts</h1></td> \
                        <td class='col-ranking text-right'><h1>" + posicao + "º</h1></td> \
                        </tr>";

                    $("#ranking tbody").append(rowTemplate);
                }
            }
        });
    }
}

$(document).ready(function() {
    index.init();
});
