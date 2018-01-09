$(document).ready(function() {
    $('#retroContentTable').DataTable({
        "order": [[ 8, "desc" ]]
    });

    $( "#id_eta" ).click(function(){
        $( "#id_eta" ).datepicker('show');
    });

    $( "#id_eta" ).on('changeDate', function(ev){
        $(this).datepicker('hide');
    });

    $('[data-toggle="tooltip"]').tooltip();

});

function exportToCSV() {
    $('#retroContentTable').tableExport({
        fileName: 'RetroReport',
        type:'csv'
    });
}
