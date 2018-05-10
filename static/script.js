$(document).ready(function(){
    $('#name').change(function() {
        $('.task-button').removeAttr('disabled');
    })

    $('.task-button').click(function(e) {
        e.preventDefault();
        var task = e.target.value;
        $('#task').val(task);
        $("#task-form").submit();
    })
});