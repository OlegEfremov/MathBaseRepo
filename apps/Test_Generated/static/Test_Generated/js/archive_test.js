function archive_test(test_id, this_el){
    $.ajax({
        url: 'archive_test',
        type: "POST",
        data: {'test_id': test_id},
        success: function(res) {
            location.reload();
        },
        error: function(ts) {
            console.log(ts)
        }
    })

    // $(this_el).closest('tr').remove();

}