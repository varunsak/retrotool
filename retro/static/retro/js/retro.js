$(document).ready(function() {
    $('#retroContentTable').DataTable();
    $( "#id_eta" ).datepicker();
});

function exportToCSV() {
    $('#retroContentTable').tableExport({
        fileName: 'RetroReport',
        type:'csv'
    });
}
