django-sorting is a pluggable app in the spirit of django-pagination.

It allows you to allow sorting on querysets, without handling them in views.

Usage
-------------

Inlude `sorting` in your `INSTALLED_APPS`

Put `{% load sorting %}` at top of your templates.

Your templates have two new tags available.

`auto_sort`
`sort_link`

The basic usage is.::

    {% sort_link "link text" "field_name" %}
    {% auto_sort queryset %}
    

sort_link
-----------------
The basic usage is.::
    
    {% sort_link "link text" "field_name" %}

Sort link outputs a link which will sort on the given field. The field to sort on should be
a database field, or something which `.order_by` of queryset would work.


Example usage.::
    
    {% sort_link "Name" "name" %}
    
It may also be used as.

    {% sort_link "link text" "field_name" "vis_name" %}

    {% sort_link "Name" "name" "what" %}
    
This is useful if you do not wnat to expose your database fields in urls.


auto_sort
-------------------

Basic usage is.::

    {% auto_sort queryset %}

It sorts the queryset in place and replaces the queryset by the sorted queryset.

This needs to be called prior to a slice has been taken from a queryset.
(Ordering can not be done after the slice has been taken.) In particular this will
not work with generuc view `object_list`.

License
-----------
This code is available under a GPL or a BSD license.


History
------------
There is a well used Django sorting library at http://github.com/directeur/django-sorting . So why another?
Well, I had this library written before I was aware of this library. :)
The libraries are fairly close in functionality. But I think mine is better in two ways. :)

0. It doesnt use a middleware
1. It allows setting a visible name which is independent of the database field.

