function init_checkbox_values() {
    if (sessionStorage.getItem('checkbox_values') == null) {
        checkbox_values = {};
        write_checkbox_values();
    } else {
        read_checkbox_values();
    }
}

function read_checkbox_values() {
    checkbox_values =  JSON.parse(sessionStorage.getItem('checkbox_values'));
}

function write_checkbox_values() {
    sessionStorage.setItem('checkbox_values', JSON.stringify(checkbox_values));
}
