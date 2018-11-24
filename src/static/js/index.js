(function($) {

    skel
		.breakpoints({
			xlarge:	'(max-width: 1680px)',
			large:	'(max-width: 1280px)',
			medium:	'(max-width: 980px)',
			small:	'(max-width: 736px)',
			xsmall:	'(max-width: 480px)'
		});

	$(function() {

		var	$window = $(window),
			$body = $('body')

		$body.addClass('is-loading');

		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-loading');
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

    $('.select-dropdown__list-item').on('click', function(){
	    var itemValue = $(this).data('value');
	    console.log(itemValue);
	    $('.select-dropdown__button span').text($(this).text()).parent().attr('data-value', itemValue);
	    $('.select-dropdown__list').toggleClass('active');
    });


})(jQuery);
