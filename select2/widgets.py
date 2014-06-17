"""
Contains some fields as utilities
"""
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from . import conf


class SelectAutocomplete(forms.Select):
    """
    jQuery Plugin documentation: http://ivaynberg.github.io/select2/
    """
    allow_multiple_selected = False

    def __init__(self,  attrs=None, choices=(), plugin_options={}):
        super(SelectAutocomplete, self).__init__(attrs, choices)
        self.plugin_options = plugin_options

    def render(self, name, value, attrs=None, choices=()):
        res = super(SelectAutocomplete, self).render(name, value, attrs, choices)
        opts = u""
        opts_dict = {u'width': u'300px'}
        opts_dict.update(self.plugin_options)
        for k, v in opts_dict.items():
            opts += u' data-{0}="{1}"'.format(k, v)

        res = mark_safe(
            u"""
            <span class="select2-init" id="select2-init-{0}"{1}></span>
            {2}
            """.format(attrs['id'], opts, res)
        )
        return res

    class Media:
        js = tuple([lib for lib in (settings.JQUERY_LIB, settings.SELECT2_LIB) if lib])
        js += (
             u'{0}select2/js/select2__init.js'.format(settings.STATIC_URL),
        )
        if settings.SELECT2_CSS_LIB:
            css = {u"all": (settings.SELECT2_CSS_LIB,)}


class SelectMultipleAutocomplete(forms.SelectMultiple):
    """
    jQuery Plugin documentation: http://ivaynberg.github.io/select2/
    """
    allow_multiple_selected = True

    def __init__(self, attrs=None, choices=(), plugin_options={}):
        super(SelectMultipleAutocomplete, self).__init__(attrs, choices)
        self.plugin_options = plugin_options

    def render(self, name, value, attrs=None, choices=()):
        res = super(SelectMultipleAutocomplete, self).render(name, value, attrs, choices)
        opts = ""
        opts_dict = {u'width': u'300px'}
        opts_dict.update(self.plugin_options)
        for k, v in opts_dict.items():
            opts += u' data-{0}="{1}"'.format(k, v)
        res = mark_safe(
            u"""
            <span class="select2-init" id="select2-init-{0}"{1}></span>
            {2}
            """.format(attrs['id'], opts, res)
        )
        return res

    class Media:
        js = tuple([lib for lib in (settings.JQUERY_LIB, settings.SELECT2_LIB) if lib])
        js += (
            u'{0}select2/js/select2__init.js'.format(settings.STATIC_URL),
        )
        if settings.SELECT2_CSS_LIB:
            css = {u"all": (settings.SELECT2_CSS_LIB,)}
