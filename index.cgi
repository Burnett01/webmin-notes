#!/usr/bin/perl
require 'webmin-notes-lib.pl';

ui_print_header(undef, $module_info{'desc'}, "", undef, 1, 1);

my @notes = list_notes();
my @table = ( );

foreach my $s (@notes) {
	push(@table, [ 
		($s->{'status'} == 1) ? '<span class="label label-success">Enabled</span>' : '<span class="label label-danger">Disabled',
		'<span class="text-'.html_escape($s->{'style'}).'">'.html_escape($s->{'style'}).'</span>',
		"<a href='edit.cgi?title=".urlize($s->{'title'}).
	       "'>".html_escape($s->{'title'})."</a>",
		html_escape($s->{'content'})
    ]);
}

print ui_form_columns_table(
	undef,
	undef,
	0,
	[ [ 'edit.cgi?new=1', $text{'index_add'} ] ],
	undef,
	[ $text{'index_status'}, $text{'index_style'}, $text{'index_title'}, $text{'index_content'} ],
	100,
	\@table,
	undef,
	0,
	undef,
	$text{'index_none'},
);

ui_print_footer('/', $text{'index'});
