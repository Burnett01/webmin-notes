#!/usr/bin/perl

require 'webmin-notes-lib.pl';
ReadParse();

my $note;

if($in{'new'}){

	ui_print_header(undef, $text{'title_create'}, "");
	$note = { };

}else{

	ui_print_header(undef, $text{'title_edit'}, "");
	my @notes = list_notes();
	($note) = grep { $_->{'title'} eq $in{'title'} } @notes;
}

print ui_form_start('save.cgi');
print ui_hidden('new', $in{'new'});
print ui_hidden('old', $in{'title'});
print ui_table_start($text{'edit_header'}, undef, 3);

print ui_table_row($text{'edit_status'},
	ui_yesno_radio('status', $note->{'status'}, 1, 0));

print ui_table_row($text{'edit_style'},
	ui_select('style', $note->{'style'}, 
      [  
         ["success", "Success"],
         ["info", "Info"],
         ["warning", "Warning"],
         ["danger", "Danger"]
      ], 1, 0
   )
);

print ui_table_row($text{'edit_title'},
	ui_textbox('title', $note->{'title'}, 40));

print ui_table_row($text{'edit_content'},
	ui_textbox('content', $note->{'content'}, 40));

print ui_table_end();

if ($in{'new'}){

	print ui_form_end([ [ undef, $text{'create'}]]);

}else{

	print ui_form_end([ 
		[ undef, $text{'save'}],
	   [ 'delete', $text{'delete'} ] 
	]);
}

ui_print_footer('', $text{'index_return'});

