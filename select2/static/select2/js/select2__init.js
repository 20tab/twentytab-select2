jQuery(function(){

    function select2_init(){
        $('.select2-init').not('.processed').each(function(){
            var id = $(this).attr('id').replace('select2-init-', '');
            if(id.indexOf("__prefix__") == -1){
                var opts = $(this).data();
                $('#'+id).select2(opts);
                $(this).addClass('processed');
            }
        });
    }

    select2_init();


    function moreItem(){
        //It capture html change event and it should select the selected item.
        //Doesn't work yet
        if($('#select2-init-'+$(this).attr('id')).hasClass('processed')){
            console.log($(this).attr('id'));
            $(this).select2('destroy');
            $('#select2-init-'+$(this).attr('id')).removeClass('processed');
            $(this).find('option').removeAttr('selected');
            $(this).find('option:last-child').attr('selected', true);
            select2_init();
        }
    }

    $('.add-row a').on('click', function(){
        select2_init();
        $('.select2-offscreen').unbind("DOMSubtreeModified");
        $('.select2-offscreen').bind("DOMSubtreeModified", moreItem);
    });


    $('.select2-offscreen').bind("DOMSubtreeModified", moreItem);

});