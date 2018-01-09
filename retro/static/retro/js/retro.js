$(document).ready(function() {
    $('#retroContentTable').DataTable({
        "order": [[ 8, "desc" ]]
    });
    $( "#id_eta" ).datepicker();
});

function exportToCSV() {
    $('#retroContentTable').tableExport({
        fileName: 'RetroReport',
        type:'csv'
    });
}
