$('.click p').click(function(){
    $('div.click')
});
$('.hide p').click(function(){
    $('div.hide').hide()
});
$('.show p').click(function(){
    $('div.hide').show()
});
$('.toggle p').click(function(){
    $('div.show p').toggle()
});
$('.slideDown p').click(function(){
    $('div.slideUp').slideDown()
});
$('.slideUp p').click(function(){
    $('div.slideUp').slideUp()
});
$('.slideToggle p').click(function(){
    $('div.slideDown').slideToggle()
});
$('.fadeIn p').click(function(){
    $('div.fadeOut p').fadeIn(4000)
});
$('.fadeOut p').click(function(){
    $('div.fadeOut p').fadeOut(4000)
});
$('.addClass p').click(function(){
    $('div.addClass p').addClass('red')
});
$('.before p').click(function(){
    $('div.before').before($('.after'));
});
$('.after p').click(function(){
    $('div.before').after($('.after'));
});
$('.append p').click(function(){
    $('body').append($('.append'))
});
$('.html p').click(function(){
    $('div.html p').html('LOL')
});
$('.attr p').click(function(){
    $('div.attr p').attr("class",'red')
});
$('.val p').click(function(){
    $('div.val input').val("1,2,3,4,5,6")
});
$('.text p').click(function(){
    $('div.text').text('Suh Dude!')
});