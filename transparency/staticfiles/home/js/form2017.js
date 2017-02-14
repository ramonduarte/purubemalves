/**
 * Created by Ramon on 12/21/2016.
 */

function getCEP(value) {
    var a = new HttpClient().get('http://cep.republicavirtual.com.br/web_cep.php?cep='
    + value + '&formato=json', function (response) {
        var r = JSON.parse(response);
        if (r['resultado'] == '1') {
            document.getElementById('id_endereco').value = r['tipo_logradouro'] + ' ' +
                r['logradouro'] + ', ';
            document.getElementById('id_bairro').value = r['bairro'];
            document.getElementById('id_cidade').value = r['cidade'];
        }
    });
}

function getAlunoInfo(value, csrf) {
    var pathname = window.location.pathname;
    // var a = new HttpClient().post('pura2017-signingform.herokuapp.com/getalunoinfo', function (response) {
    var a = new HttpClient().post(pathname + 'getalunoinfo', value, csrf, function (response) {
    // var a = new HttpClient().post('pura2017-signingform.herokuapp.com/getalunoinfo', function (response) {
        var r = JSON.parse(response);
        if (r['success'] == '1') {
            // Data from Aluno
            document.getElementById('id_aluno_id').value = value;
            document.getElementById('id_nome').value = r['nome'];
            document.getElementById('id_cpf').value = r['cpf'];
            document.getElementById('id_data_de_nascimento_day').value = r['data_day'];
            document.getElementById('id_data_de_nascimento_month').value = r['data_month'];
            document.getElementById('id_data_de_nascimento_year').value = r['data_year'];

            // Data from Endereço
            document.getElementById('id_cep').value = r['cep'];
            document.getElementById('id_endereco').value = r['endereco'];
            document.getElementById('id_bairro').value = r['bairro'];
            document.getElementById('id_cidade').value = r['cidade'];

            // Data dfrom Contato
            document.getElementById('id_contato').value = r['contato'][0];
            document.getElementById('id_principal').value = r['principal'][0];
            document.getElementById('checkPrincipal').checked = r['principal'][0];

            if (r['contato'].length > 1) {
                for (var i = 2; i <= r['contato'].length; i++) {
                    addContact(document.getElementById('add_contact').previousSibling);
                    document.getElementById('id_contato' + i).value = r['contato'][i-1];
                    document.getElementById('id_principal' + i).value = r['principal'][i-1];
                    document.getElementById('checkPrincipal' + i).checked = r['principal'][i-1];
                }
            }

            // Data from Canais
            document.getElementById('id_redes_sociais').checked = r['redes_sociais'];
            document.getElementById('id_tv').checked = r['tv'];
            document.getElementById('id_radio').checked = r['radio'];
            document.getElementById('id_jornal_impresso').checked = r['jornal_impresso'];
            document.getElementById('id_jornal_internet').checked = r['jornal_internet'];
            document.getElementById('id_blogs').checked = r['blogs'];

            // Data from Acesso
            document.getElementById('id_acesso_a_internet').checked = r['acesso_a_internet'];
            toggle(document.getElementById('id_acesso_a_internet'), 'modo_de_acesso');

            //Data from Modo de Acesso
            document.getElementById('id_pc_domestico').checked = r['pc_domestico'];
            document.getElementById('id_pc_trabalho').checked = r['pc_trabalho'];
            document.getElementById('id_celular').checked = r['celular'];
            document.getElementById('id_pc_conhecido').checked = r['pc_conhecido'];
            document.getElementById('id_lan_house').checked = r['lan_house'];

            // Data from Curso
            document.getElementById('id_curso').value = r['curso_pretendido'];
            document.getElementById('id_lingua').value = r['lingua'];

            // Data from Ensino Médio
            document.getElementById('id_ano_de_conclusao').value = r['ano_de_conclusao'];
            document.getElementById('id_ensino_medio_concluido').checked = r['ensino_medio_concluido'];
            document.getElementById('id_escola').value = r['escola'];
            document.getElementById('id_tipo_de_escola').value = r['tipo_de_escola'];

            // Data from Pré-Vestibular
            document.getElementById('id_fez_prevest').checked = r['fez_prevest'];
            toggle(document.getElementById('id_fez_prevest'), 'div_prevest');
            document.getElementById('id_prevest').value = r['prevest'];

            // Data from Faculdade
            document.getElementById('id_fez_faculdade').checked = r['fez_faculdade'];
            toggle(document.getElementById('id_fez_faculdade'), 'div_faculdade');
            document.getElementById('id_faculdade').value = r['faculdade'];
            document.getElementById('id_faculdade_curso').value = r['faculdade_curso'];
            document.getElementById('id_tipo_de_faculdade').value = r['tipo_de_faculdade'];
            switch (r['ja_trabalhou']) {
                case 0:
                    document.getElementById('id_ja_trabalhou').value = 'False';
                    break;
                case 1:
                    document.getElementById('id_ja_trabalhou').value = 'True';
                    break;
            }
            switch (r['empregado']) {
                case 0:
                    document.getElementById('id_empregado').value = 'False';
                    break;
                case 1:
                    document.getElementById('id_empregado').value = 'True';
                    break;
            }
            document.getElementById('id_renda').value = r['renda'];
            document.getElementById('id_objetivo').value = r['objetivo'];
            document.getElementById('id_ex_aluno').checked = r['ex_aluno'];
            document.getElementById('id_como_conheceu').value = r['como_conheceu'];
            document.getElementById('id_motivacao').value = r['motivacao'];
            document.getElementById('id_comentario').value = r['comentario'];
        }
    });
}

var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() {
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }

        anHttpRequest.open( "GET", aUrl, true );
        anHttpRequest.send( null );
    }
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
        // var anHttpRequest = new XMLHttpRequest();
        // anHttpRequest.onreadystatechange = function() {
        //     if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
        //         aCallback(anHttpRequest.responseText);
        // }
        // anHttpRequest.open( "POST", aUrl, true );
        // anHttpRequest.setRequestHeader('csrfmiddlewaretoken', csrf);
        // anHttpRequest.setRequestHeader('id', value);
        // anHttpRequest.send( value );
    }
}

function toggle(element) {
    if (element.checked) {
        for (var i = 1; i < arguments.length; i++)
            document.getElementById(arguments[i]).setAttribute("style", "display: block");
    } else {
        for (var j = 1; j < arguments.length; j++)
            document.getElementById(arguments[j]).setAttribute("style", "display: none");
    }
}
function toggleOnClick(block) {
    if (block.getAttribute("style") == "display: block")
        block.setAttribute("style", "display: none");
    else
        block.setAttribute("style", "display: block");
}

function addContact(element) {
    var numberOfContacts = document.getElementsByName('contato').length + 1;
    var contact = element.cloneNode(true);
    contact.setAttribute('id', 'div-contato' + numberOfContacts);
    contact.children[0].setAttribute('for', 'id_contato' + numberOfContacts);
    contact.children[1].setAttribute('id', 'id_contato' + numberOfContacts);
    contact.children[1].value = '';
    contact.children[1].required = false;
    contact.children[2].setAttribute('id', 'id_principal' + numberOfContacts);
    contact.children[2].setAttribute('value', '0');
    contact.children[3].setAttribute('id', 'checkPrincipal' + numberOfContacts);
    // contact.children[3].setAttribute('onchange', 'document.getElementById("hiddenPrincipal' + numberOfContacts + '").value += 1');
    contact.children[3].checked = false;
    contact.children[4].setAttribute('for', 'checkPrincipal' + numberOfContacts);
    element.parentNode.insertBefore(contact, element.nextSibling);
}

