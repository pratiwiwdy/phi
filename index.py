<!DOCTYPE html>
<html>
<head>
    <title>Golden Ratio Visualization</title>
    <style>
        #phi {
            width: 50%;
            height: 50%;
            position: absolute;
            top: 25%;
            left: 25%;
            background-color: #ff2c5a;
        }
        #phi:before {
            content: "";
            display: block;
            padding-top: 61.8%;
        }
    </style>
</head>
<body>
    <div id="phi"></div>
    <script>
        // Golden Ratio
        var phi = (1 + Math.sqrt(5)) / 2;

        // Get the div element
        var div = document.getElementById('phi');

        // Set the width and height of the div to visualize the golden ratio
        div.style.width = '100%';
        div.style.height = (100 / phi) + '%';
    </script>
</body>
</html>
