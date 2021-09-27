$( document ).ready(function() {
    var ventana_alto = $(window).height();
    $('.swiper-slide').css('height', ventana_alto);

    
    $('.usuario').css('min-height', ventana_alto);

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
});