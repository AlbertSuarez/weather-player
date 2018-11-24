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
/*            var newWin = window.open("/auth", "Spotify Login", "width=500,height=500");
            $(newWin).unload(function(){
                alert(newWin.location.href);
                alert(newWin.location.href.includes('/callback'));
                if (newWin.location.href.includes('/callback')){
                    var myPlay = document.getElementById('play');
                    var myLoader = document.getElementById('load');
                    myPlay.style.display = 'none';
                    myLoader.style.display = 'block';
                    var newUrl = '/playlist?weather=' + $('#weather').text() + '&feeling=' + itemValue;
                    newWin.opener.location = newUrl;
                    newWin.close();
                    console.log("I closed :)");
                }
            });*/
        }
    })

})(jQuery);
