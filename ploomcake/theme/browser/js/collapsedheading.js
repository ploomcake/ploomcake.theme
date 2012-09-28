(function ($){
    $(".collapsedHeading").live('click',function (){
        var $heading = $(this);
        $heading
            .next()
            .slideToggle(200 ,function (){
                $heading.toggleClass('collapsed');
            });
    });
}(jQuery));



