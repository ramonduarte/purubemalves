/**
 * Created by Ramon on 3/7/2017.
 */

var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() {
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        };

        anHttpRequest.open( "GET", aUrl, true );
        anHttpRequest.send( null );
    };
    this.post = function(aUrl, value, csrf, aCallback) {
        $.ajax({
            url: aUrl,
            type: "POST",
            data: {id: value, 'csrfmiddlewaretoken': csrf},
            success: function(data) {
                aCallback(data);
                console.log(data);
            }
        });
    }
};

function getCEP(value) {
    var a = new HttpClient().get('/getcep?cep='
    + value, function (response) {
        var r = JSON.parse(response);
        if (r['resultado'] == '1') {
            document.getElementById('id_endereco').value = r['tipo_logradouro'] + ' ' +
                r['logradouro'] + ', ';
            document.getElementById('id_bairro').value = r['bairro'];
            document.getElementById('id_cidade').value = r['cidade'];
            document.getElementById('id_estado').value = r['uf'];
        }
    });
}

django.jQuery(document).ready(function( ) {
    django.jQuery('#id_cep').blur(function () {
        getCEP(django.jQuery(this).val());
    });
});