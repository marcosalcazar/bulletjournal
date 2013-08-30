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
    $(".item input[type='checkbox'].completed").change(function(){
    	var el = $(this);
    	var url = el.attr('action');
    	$.post(url, {
    		'completed': el.prop('checked')
    	}, function(data){
    		console.log(data);
    	});
    });
    $(".item select.indicator").change(function(){
    	var el = $(this);
    	var url = el.attr('action');
    	$.post(url, {
    		'indicator': el.val()
    	}, function(data){
    		console.log(data);
    	});
    });
});
