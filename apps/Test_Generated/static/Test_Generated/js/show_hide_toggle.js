function show_hide_toggle(y, display_type = 'block') {
    for (var i=0; i<y.length; i++)
        {
            var x = y[i];
            if (x.style.display === "none") {
                x.style.display = display_type;
            } else {
                x.style.display = "none";
            }
        }
}