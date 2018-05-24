$(document).ready(function() {
    $( "#id_eta" ).click(function(){
        $( "#id_eta" ).datepicker('show');
    });

    $( "#id_eta" ).on('changeDate', function(ev){
        $(this).datepicker('hide');
    });

    $('[data-toggle="tooltip"]').tooltip();

    var table = $('#retroContentTable').DataTable( {
        "order": [],
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Create',
                action: function ( e, dt, node, config ) {
                    window.location.href = '/create';
                }
            }
        ]
    } );

    new $.fn.dataTable.Buttons( table, {
        buttons: [
            { extend: 'csv', text: 'Export' }
        ]
    } );

    table.buttons( 1, null ).container().appendTo(
        table.table().container()
    );

});
