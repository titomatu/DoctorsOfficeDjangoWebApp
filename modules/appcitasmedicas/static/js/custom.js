$( document ).ready(function() {
    var ventana_alto = $(window).height();
    $('.swiper-slide').css('height', ventana_alto);

    
    $('.usuario').css('min-height', ventana_alto);
    $('.cont-img-lateral').css('min-height', ventana_alto);

    var Swipes = new Swiper('.swiper-container', {
        loop: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        pagination: {
            el: '.swiper-pagination',
        },
    }); 
    $( ".item-solicitar" ).click(function() {
        $('.box-contenido-usuario').css('display','none');
          $('#box-agendar').css('display','block');
      });
      $( ".item-consultar" ).click(function() {
        $('.box-contenido-usuario').css('display','none');
          $('#box-consultar').css('display','block');
      });
      $( ".item-cancelar" ).click(function() {
        $('.box-contenido-usuario').css('display','none');
          $('#box-cancelar').css('display','block');
      });
         
});

$( window ).resize(function() {
    var ventana_alto = $(window).height();
    $('.swiper-slide').css('height', ventana_alto);

    
    $('.usuario').css('min-height', ventana_alto);
    $('.cont-img-lateral').css('min-height', ventana_alto);
});