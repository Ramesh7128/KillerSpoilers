$(document).ready(function(){

    var csrftoken = $.get('csrftoken');
    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $("#suggestionsform").submit(function(event) {
    event.preventDefault();
    var name = $("input#name").val();
    var email = $("input#email").val();
    var phone = $("input#phone").val();
    var suggestions = $("textarea#message").val();

    data_dict = {
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "suggestions":suggestions,
    }

    $.post('/', data_dict,
                function(
                    data, status) {
                    console.log(data, "asldnaksdna");
                    console.log(status,"dsknkjsd");
                    if (data == "success") {

                        $('#status_msg').html(
                                '<div class="alert alert-success fade in"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>Thank you!</strong>.We shall make sure we will add the tv show u suggested, asap.</div>'
                         );
                        $("#suggestionsform")[0].reset();
                        

                        console.log('success');
                
                    } else {

                        $('#status_msg').html(
                                '<div class="alert alert-warning fade in"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>Sorry!</strong> Your suggestion did not get submitted.Kindly do it again after some time</div>'
                            )
                        $("#suggestionsform")[0].reset();
                        console.log('error');
                    }
    });
    });

});