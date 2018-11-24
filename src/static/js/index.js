(function($) {

    skel
        .breakpoints({
            xlarge: '(max-width: 1680px)',
            large:  '(max-width: 1280px)',
            medium: '(max-width: 980px)',
            small:  '(max-width: 736px)',
            xsmall: '(max-width: 480px)'
        });

    $(function() {

        var $window = $(window),
            $body = $('body')

        $body.addClass('is-loading');

        $window.on('load', function() {
            window.setTimeout(function() {
                $body.removeClass('is-loading');
                $('iframe').addClass('change-shit');
            }, 100);
        });

        if (skel.vars.mobile)
            $body.addClass('is-mobile');
        else
            skel
                .on('-medium !medium', function() {
                    $body.removeClass('is-mobile');
                })
                .on('+medium', function() {
                    $body.addClass('is-mobile');
                });

    });

    $('.select-dropdown__button').on('click', function(){
        $('.select-dropdown__list').toggleClass('active');
    });

    var itemValue = null
    $('.select-dropdown__list-item').on('click', function(){
        itemValue = $(this).data('value');
        console.log(itemValue);
        $('#input_feeling').val(itemValue);
        $('.select-dropdown__button span').text($(this).text()).parent().attr('data-value', itemValue);
        $('.select-dropdown__list').toggleClass('active');
    });

    $('#play').on('click', function(){
        if (itemValue == null) {
            window.alert("C'mon, don't be shy! How are you feeling?");
        } else {
            $('#form_submit').submit();
        }
    })

})(jQuery);
