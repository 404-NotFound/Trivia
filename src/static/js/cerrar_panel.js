jQuery(document).ready(function($) {
	$('body').click(function() {
		$(".collapse").collapse('hide');
	  if (!$(this.target).is('#userPanel')) {
		  $(".collapse").collapse('hide');
	  }
	});
} );