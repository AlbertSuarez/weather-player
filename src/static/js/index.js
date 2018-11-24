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

		skel.on('+medium -medium', function() {
			$.prioritize(
				'.important\\28 medium\\29',
				skel.breakpoint('medium').active
			);
		});

	});

})(jQuery);
