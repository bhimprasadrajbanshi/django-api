# django-Rest- framework-api
<h3>This project only for basic api like get(read data) funtion</h3>

## Declaring Serializers
#### We'll declare a serializer that we can use to serialize and deserialize data that corresponds to student objects.
<p> Declaring a serializer like similar to declaring a form </p>

```python

  class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    addres = serializers.CharField(max_length=200)
```
## Serializing objects

```python
  serializer = studentSerializer(std)
```
<p>To finalise the serialization process we render the data into json</p>
from rest_framework.renderers import JSONRenderer

```python
  json = JSONRenderer().render(serializer.data)
```

# Example
<p>To get the example project running do</p>
<p>1)Clone this repo </p> 

```bash
  https://github.com/bhimprasadrajbanshi/django-api.git
```

</p> 2)install virtual enviroment</p> 

```bash
  py -m venv env
```

</p> 3)nstall all of the Python modules and packages listed in your requirements.txt file</p> 

```bash
 pip install -r requirements.txt
```

<p>.admin user:asus</p>
<p>.admin password:123</p>


