# webmin-notes

A small module that allows you to create/edit/remove notes.

* [General usage](#general-usage)
* [Example usage (authentic-theme theme)](#example-usage-authentic-theme-theme)
* [Example usage (winfuture Bootstrap theme)](#example-usage-winfuture-bootstrap-theme)
* [API](#api)

---

## General usage
Add the following in your template file (body.cgi or index.cgi):

```perl
&foreign_require("webmin-notes");
@notes = &webmin_notes::list_notes();
foreach my $n (@notes) {
	#now you have access to each note
	#Available methods: status, style, title, content
}
```

---

## Example usage (authentic-theme theme):

<img src="https://i.imgur.com/1UyqoYZ.png"/>

<img src="https://i.imgur.com/w5JV5ql.png"/>

<img src="https://i.imgur.com/TAImqi1.png"/>

This example fits authentic-theme (https://github.com/virtualmin/authentic-theme).

Edit ``/usr/share/webmin/authentic-theme/sysinfo.cgi`` and add the following code on line ``22``:

```perl
&foreign_require("webmin-notes", "webmin-notes-lib.pl");
my @notes = &webmin_notes::list_notes();

foreach my $n (@notes) {
	if ($n->{'status'} == 1) {
		print '<div class="alert alert-'. html_escape($n->{'style'}) .'" role="alert"><b>'. html_escape($n->{'title'}) .'</b> '. html_escape($n->{'content'}) . "</div>\n";
	}
}
```

---

## Example usage (winfuture Bootstrap theme):

<img src="http://i.imgur.com/Yfa6rDI.png"/>

<img src="http://i.imgur.com/R1pTHFp.png"/>

<img src="http://i.imgur.com/H7GItww.png"/>

This example fits @winfuture Bootstrap theme (http://theme.winfuture.it/).

Edit the ``index.cgi`` of the theme and add the following code:

```perl
&foreign_require("webmin-notes");
@notes = &webmin_notes::list_notes();
foreach my $n (@notes) {
	if ($n->{'status'} == 1) {
		print '<div class="alert alert-'. html_escape($n->{'style'}) .'" role="alert"><b>'. html_escape($n->{'title'}) .'</b> '. html_escape($n->{'content'}) . "</div>\n";
	}
}
```

---

---

## API

### Methods

```perl
::list_notes()
::create_note($note)
::modify_note($note)
::delete_note($note)
```

### Hashmap ($note)

```perl

| Key        | Value           
| ------------- |:-------------:
| status      	| 0 = disabled / 1 = enabled
| style      	| warning, info, danger, success
| title      	| note-title
| content      	| note-content


```

---

## Download:

http://www.webmin.com/cgi-bin/search_third.cgi?search=Webmin-Notes
