(function ($){
    $(document).ready(function (){
        var $searchField = $('.searchField, .searchPage[type=text]');
//        var $searchReset = $('<input class="searchReset resetbutton" type="button" value="⨯"/>').insertAfter($searchField);
        var $searchReset = $('<a class="searchReset resetbutton">⨯</a>').insertAfter($searchField);

        $searchField.keyup(function (){
            var $this = $(this);
            if($this.val()){
                $this.next('.searchReset').css('visibility','visible');
            }
            else{
                $this.next('.searchReset').css('visibility','hidden');
            }
        });

        $searchReset.click(function (){
            var $this = $(this);
            $this.prev().val('').focus();
            $this.css('visibility','hidden');
            return false;
        });

    });
}(jQuery));
