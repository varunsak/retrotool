$(document).ready(function() {
    $('#retroContentTable').DataTable({
        "order": [[ 8, "desc" ]]
    });
    $( "#id_eta" ).click(function(){
         $( "#id_eta" ).datepicker('show');
    });
});

function exportToCSV() {
    $('#retroContentTable').tableExport({
        fileName: 'RetroReport',
        type:'csv'
    });
}
