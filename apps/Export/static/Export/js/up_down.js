function up_down(node) {
        var tempScrollTop = $(document).scrollTop();
        var row = $(node).parents('tr:first');
        if ($(node).is('.up')) {
            if (row.index() !== 0){
                //renumber rows
                document.getElementById('order_number_'+row.attr('id')).innerHTML = '№' + row.index().toString();
                document.getElementById('order_number_'+row.prev('tr').attr('id')).innerHTML = '№'+(row.prev('tr').index()+2).toString();
                row.insertBefore(row.prev());

                var ans_row = $('#task'+row.attr('id'))
                document.getElementById('ans_order_number_'+ans_row.attr('id')).innerHTML = '№' + ans_row.index().toString();
                document.getElementById('ans_order_number_'+ans_row.prev('tr').attr('id')).innerHTML = '№'+(ans_row.prev('tr').index()+2).toString();
                ans_row.insertBefore(ans_row.prev());
            }
        } else {
            if (row.next('tr').length !== 0) {
                //renumber rows
                document.getElementById('order_number_' + row.attr('id')).innerHTML = '№' + (row.index() + 2).toString();
                document.getElementById('order_number_' + row.next('tr').attr('id')).innerHTML = '№' + (row.next('tr').index()).toString();
                row.insertAfter(row.next());

                var ans_row = $('#task'+row.attr('id'));
                document.getElementById('ans_order_number_' + ans_row.attr('id')).innerHTML = '№' + (ans_row.index() + 2).toString();
                document.getElementById('ans_order_number_' + ans_row.next('tr').attr('id')).innerHTML = '№' + (ans_row.next('tr').index()).toString();
                ans_row.insertAfter(ans_row.next());

            }
        }
        $(document).scrollTop(tempScrollTop);
        return false
};
