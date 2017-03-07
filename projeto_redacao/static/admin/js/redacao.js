/**
 * Created by Ramon on 3/7/2017.
 */
django.jQuery(document).ready(function() {
    django.jQuery('#id_competencia5').blur(function () {
        django.jQuery('#id_nota').val(
            parseFloat(django.jQuery('#id_competencia1').val()) +
            parseFloat(django.jQuery('#id_competencia2').val()) +
            parseFloat(django.jQuery('#id_competencia3').val()) +
            parseFloat(django.jQuery('#id_competencia4').val()) +
            parseFloat(django.jQuery('#id_competencia5').val())
        );
    });
});
