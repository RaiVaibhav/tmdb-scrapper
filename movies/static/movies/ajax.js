$(function(){

    $('#query').keyup(function(){

        $.ajax({
            type: 'POST',
            url: '/movies/',
            data:{
                'search_text': $('#query').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#result').html(data);
}