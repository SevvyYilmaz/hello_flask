
#<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='/css/style.css') }}">
#<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
#<!-- linking an image -->
<img src="{{ url_for('static', filename='my_img.png') }}">

