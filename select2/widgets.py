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
        if self.plugin_options:
            for k, v in self.plugin_options.items():
                opts += u' data-{}="{}"'.format(k, v)

        res = mark_safe(
            u"""
            <span class="select2-init" id="select2-init-{}"{}></span>
            {}
            """.format(attrs['id'], opts, res)
        )
        return res

    class Media:
        js = (
            settings.JQUERY_LIB,
            u'{}select2/{}/select2.min.js'.format(settings.STATIC_URL, settings.SELECT2_VERSION),
            u'{}select2/js/select2__init.js'.format(settings.STATIC_URL),
        )
        css = {u"all": (u"{}select2/{}/select2.css".format(settings.STATIC_URL, settings.SELECT2_VERSION),)}


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
        if self.plugin_options:
            for k, v in self.plugin_options.items():
                opts += u' data-{}="{}"'.format(k, v)
        res = mark_safe(
            u"""
            <span class="select2-init" id="select2-init-%s"%s></span>
            {}
            """.format(attrs['id'], opts, res)
        )
        return res

    class Media:
        js = (
            settings.JQUERY_LIB,
            u'{}select2/{}/select2.min.js'.format(settings.STATIC_URL, settings.SELECT2_VERSION),
            u'{}select2/js/select2__init.js'.format(settings.STATIC_URL),
        )
        css = {u"all": (u"{}select2/{}/select2.css".format(settings.STATIC_URL, settings.SELECT2_VERSION),)}
