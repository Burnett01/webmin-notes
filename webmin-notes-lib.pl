use WebminCore;
init_config();

sub list_notes
{
	my @rv;
	my $lnum = 0;

	open(CONF, $config{'notes_conf'});

	while(<CONF>) {
		s/\r|\n//g;
		s/#.*$//;
		my ($status, $style, $title, $content) = split(/\|/, $_);

		if($content){

			push(@rv, { 
				'status' => $status,
				'style' => $style,
				'title' => $title,
				'content' => $content,
				'line' => $lnum 
			});
		}
		$lnum++;
		}
	close(CONF);
	return @rv;
}


sub create_note
{
	my ($note) = @_;
	open_tempfile(CONF, ">>$config{'notes_conf'}");
	print_tempfile(CONF, $note->{'status'}."|".$note->{'style'}."|".$note->{'title'}."|".$note->{'content'}."\n");
	close_tempfile(CONF);
}


sub modify_note
{
	my ($note) = @_;
	my $lref = read_file_lines($config{'notes_conf'});
	$lref->[$note->{'line'}] = $note->{'status'}."|".$note->{'style'}."|".$note->{'title'}."|".$note->{'content'};
	flush_file_lines($config{'notes_conf'});
}

sub delete_note
{
	my ($note) = @_;
	my $lref = read_file_lines($config{'notes_conf'});
	splice(@$lref, $note->{'line'}, 1);
	flush_file_lines($config{'notes_conf'});
}


sub apply_configuration
{
   kill_byname_logged('HUP', 'noted');
}

1;

