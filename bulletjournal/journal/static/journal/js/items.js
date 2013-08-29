function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        }
    }
});


$(document).ready(function() {
    $(".item input[type='checkbox'].completed").click(function(){
    	var el = $(this);
    	var url = el.attr('action');
    	console.log(el.prop('checked'))
    	$.post(url, {
    		'completed': el.prop('checked')
    	}, function(data){
    		console.log(data);
    	});
    })
});
