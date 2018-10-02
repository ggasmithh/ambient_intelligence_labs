$(document).ready(function () {
    $("#tasklist").append("<ul></ul>");

    $.getJSON("http://127.0.0.1:5000/api/v1.0/tasks", function(data){
        var tasks = data["tasks"] ;
        var len = tasks.length ;
        for(var i = 0 ; i<len ; i++) {
            var t = tasks[i] ;
             $("#tasklist ul").append("<li>"+t.description+"</li>") ;
        }
    }) ;

    $("#addForm").submit( function(){
        var description = $("#taskDescription").val() ;


        return false ; // don't submit the form
    }) ;
});

function addTask(){

}