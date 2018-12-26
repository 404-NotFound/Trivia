(document).ready(window.onload = function(){
  var x = document.getElementById("mejor_tf");
  var y = document.getElementById("ganadas");
  var z = document.getElementById("sabelotodo");
  x.style.display = "block";
  y.style.display = "none";
  z.style.display = "none";
  
});
function mejor_tfDiv() {
  $("#btnX").removeClass("active");
  $('#btnX').button('toggle');
  $('#btnY').button('dispose');
  $('#btnZ').button('dispose');
  var x = document.getElementById("mejor_tf");
  var y = document.getElementById("ganadas");
  var z = document.getElementById("sabelotodo");
  x.style.display = "block";
  y.style.display = "none";
  z.style.display = "none";
}
function ganadasDiv() {
  $("#btnX").removeClass("active");
  $('#btnX').button('dispose');
  $('#btnY').button('toggle');
  $('#btnZ').button('dispose');
  var x = document.getElementById("mejor_tf");
  var y = document.getElementById("ganadas");
  var z = document.getElementById("sabelotodo");
  x.style.display = "none";
  y.style.display = "block";
  z.style.display = "none";
}
function sabelotodoDiv() {
  $("#btnX").removeClass("active");
  $('#btnX').button('dispose');
  $('#btnY').button('dispose');
  $('#btnZ').button('toggle');
  var x = document.getElementById("mejor_tf");
  var y = document.getElementById("ganadas");
  var z = document.getElementById("sabelotodo");
  x.style.display = "none";
  y.style.display = "none";
  z.style.display = "block";
}