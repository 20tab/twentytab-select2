twentytab-select2
=================

A Django widget with [Select2](http://ivaynberg.github.com/select2/) integration. 

## Installation

Use the following command: <b><i>pip install twentytab-select2</i></b>

## Configuration

- Settings.py

Open settings.py and add select2 to your INSTALLED_APPS:

```py
INSTALLED_APPS = {
    ...,
    'select2',
    ...
}
```

- Static files

Run collectstatic command or map static directory. If you use uWSGI you can map static files:

```ini
static-map = /static/select2/=%(path_to_site_packages)/select2/static/select2
```

## Usage

- forms.py

```py

from testapp.models import ModelTest
from django import forms
from select2.widgets import SelectAutocomplete


class TestForm(forms.ModelForm):
    class Meta:
        model = ModelTest
        widgets = {
            'myfield': SelectAutocomplete(plugin_options={"width": "300px"}),
        }


```
