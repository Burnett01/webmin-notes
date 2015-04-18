#!/usr/bin/perl

require 'webmin-notes-lib.pl';
ReadParse();
error_setup($text{'save_err'});
lock_file($config{'notes_conf'});

# Get the old site object
if (!$in{'new'}) {
	my @notes = list_notes();
        ($note) = grep { $_->{'title'} eq $in{'old'} } @notes;
	$note || error($text{'save_egone'});
	}

if ($in{'delete'}) {

	delete_note($note);

}else{

	#style regex needs a fix (case sens)
	$in{'style'} =~ /^(warning|info|danger|success)+$/i ||
		error($text{'save_estyle'});

	$in{'title'} =~ /^[A-Za-z0-9\-\_\.\[\]\(\)\%\&\!\?\/\,\s]+$/i ||
		error($text{'save_etitle'});

	$in{'content'} =~ /^[A-Za-z0-9\-\_\.\[\]\(\)\%\&\!\?\/\,\s]+$/i ||
		error($text{'save_econtent'});
	
	$note->{'status'} = $in{'status'};
	$note->{'style'} = $in{'style'};
	$note->{'title'} = $in{'title'};
	$note->{'content'} = $in{'content'};

	# Update or create
	if ($in{'new'}){

		create_note($note);

	}else{

		modify_note($note);
	}
}

# Log the change
unlock_file($config{'notes_conf'});
apply_configuration();

webmin_log($in{'new'} ? 'create' :
   $in{'delete'} ? 'delete' : 'modify',
   'note',
   $note->{'title'}
);

&redirect('');

