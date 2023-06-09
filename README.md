# django-Rest- framework-api
<h3>This project only for basic api like get(read data) funtion</h3>

# Example
<p>To get the example project running do</p>
<p>1)Clone this repo</p>
$https://github.com/bhimprasadrajbanshi/django-api.git

<p>2)admin user:asus</p>
<p>3)admin password:123</p>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <div id="secretInfo" style="display: none;">secret info</div>
    <button type="button" id="btnCopy">Copy hidden info</button>

    <script type="text/javascript">
      var $body = document.getElementsByTagName('body')[0];
      var $btnCopy = document.getElementById('btnCopy');
      var secretInfo = document.getElementById('secretInfo').innerHTML;

      var copyToClipboard = function(secretInfo) {
        var $tempInput = document.createElement('INPUT');
        $body.appendChild($tempInput);
        $tempInput.setAttribute('value', secretInfo)
        $tempInput.select();
        document.execCommand('copy');
        $body.removeChild($tempInput);
      }

      $btnCopy.addEventListener('click', function(ev) {
        copyToClipboard(secretInfo);
      });
    </script>
  </body>
</html>

