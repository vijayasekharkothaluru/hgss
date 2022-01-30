var text = $('#id_text').val();
var stat = $('#id_start').val();
var las = $('#id_end').val();
var st1 = text.slice(0,parseInt(stat))
var st2 = text.slice(parseInt(stat), parseInt(las))
var st3 = text.slice(parseInt(las))
$('.st1').text(st1);
$('.st2').text(st2);
$('.st3').text(st3);
$('.st2').css("background-color", "yellow");



