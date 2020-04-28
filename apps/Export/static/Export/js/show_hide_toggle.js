function show_hide_toggle(y, display_type = 'block') {
    for (var i=0; i<y.length; i++)
        {
            var x = y[i];
            if (x.style.display === "none") {
                x.style.display = display_type;

                document.cookie = x.className + "=" + display_type + "; path=/";
            } else {
                x.style.display = "none";
                document.cookie = x.className + "=none" + "; path=/";
            }
        }
}
