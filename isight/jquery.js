$(document).ready(function(){
    var $regexname=/^([a-zA-Z]{3,16})$/;
    $('#alphabet').on('keypress keydown keyup',function(){

             if (!$(this).val().match($regexname)) {
              // there is a mismatch, hence show the error message
                 $('.emsg').removeClass('hidden');
                 $('.emsg').show();
             }
           else{
                // else, do not display message
                $('.emsg').addClass('hidden');
               }
         });
});

$(document).ready(function(){
    var $regexname=/^([a-zA-Z]{3,16})$/;
    $('#date').on('keypress keydown keyup',function(){

             if (!$(this).val().match($regexname)) {
              // there is a mismatch, hence show the error message
                 $('.emsg').removeClass('hidden');
                 $('.emsg').show();
             }
           else{
                // else, do not display message
                $('.emsg').addClass('hidden');
               }
         });
});
