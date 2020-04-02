function print_as_pdf(div_id){
    // var doc = new jsPDF()
    //
    // doc.text('Hello world!', 10, 10)
    // doc.save('a4.pdf')

    var doc = new jsPDF();
    var specialElementHandlers = {
        '#table_of_tasks': function (element, renderer) {
            return true;
        }
    };


    doc.fromHTML($('#content').html(), 15, 15, {
        'width': 170,
            'elementHandlers': specialElementHandlers
    });
    doc.save('sample-file.pdf');


}