twentytab-select2
=================

A Django widget with [Select2](http://ivaynberg.github.com/select2/) integration. 

## Installation

Use the following command: <b><i>pip install twentytab-select2</i></b>

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