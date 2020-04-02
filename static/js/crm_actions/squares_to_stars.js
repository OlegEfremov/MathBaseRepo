function squares_to_stars(){
    for (var k in square_values){
        if (square_values[k]){
            checkbox_values[k.replace('square', 'checkbox')] = true
        }
    }

    write_checkbox_values()
}
