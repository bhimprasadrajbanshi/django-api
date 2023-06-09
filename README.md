# django-Rest- framework-api
<h3>This project only for basic api like get(read data) funtion</h3>

# Example
<p>To get the example project running do</p>
<p>1)Clone this repo</p>
$https://github.com/bhimprasadrajbanshi/django-api.git

<p>2)admin user:asus</p>
<p>3)admin password:123</p>

var copy = function(target) {
    var textArea = document.createElement('textarea')
    textArea.setAttribute('style','width:1px;border:0;opacity:0;')
    document.body.appendChild(textArea)
    textArea.value = target.innerHTML
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
}
var pres = document.querySelectorAll(".comment-body > pre")
pres.forEach(function(pre){
  var button = document.createElement("button")
  button.className = "btn btn-sm"
  button.innerHTML = "copy"
  pre.parentNode.insertBefore(button, pre)
  button.addEventListener('click', function(e){
    e.preventDefault()
    copy(pre.childNodes[0])
  })
})
