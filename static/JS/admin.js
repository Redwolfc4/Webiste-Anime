$(document).ready(function() {
    $('.toggler-icon').click(function(){
        $('#hamburger-menu').toggleClass('change');
        $('ul').toggleClass('active');
    });
});