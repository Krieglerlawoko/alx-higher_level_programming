$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (d) {
    $('DIV#hello').text(d.hello);
  });
});
