$(document).ready(function() {
    /*$('#retroContentTable').DataTable({
        "bSort": false
    });*/

    $( "#id_eta" ).click(function(){
        $( "#id_eta" ).datepicker('show');
    });

    $( "#id_eta" ).on('changeDate', function(ev){
        $(this).datepicker('hide');
    });

    $('[data-toggle="tooltip"]').tooltip();

    /*$('#retroContentTable').excelTableFilter();*/

    $('#retroContentTable').dataTable({
        /* No ordering applied by DataTables during initialisation */
        "order": []
    });

});

function exportToCSV() {
    $('#retroContentTable').tableExport({
        fileName: 'RetroReport',
        type:'csv'
    });
}
