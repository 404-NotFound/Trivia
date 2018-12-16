jQuery(document).ready(function($) {
var hash=window.location.hash;
if ( hash=='' || hash=='#' || hash==undefined ) return false;
  var target=$(hash);
  target=target.length ? target : $('[name=' + hash.slice(1) +']');
  if (target.length) {
	  $('html,body').stop().animate({scrollTop: (target.offset().top - 70)},1,"easeInOutExpo");
    }
} );