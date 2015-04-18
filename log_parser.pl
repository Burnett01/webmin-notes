# log_parser.pl
# Functions for parsing this module's logs

require 'webmin-notes-lib.pl';

sub parse_webmin_log
{
	my ($user, $script, $action, $type, $object, $p) = @_;
	return &text('log_'.$action, '<tt>'.html_escape($object).'</tt>');
}

