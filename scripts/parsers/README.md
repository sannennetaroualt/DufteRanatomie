# Parsers

Every CSV file corresponds to a particular note type, and for every note type there's supposed to be a separate parser. This is actually a lie, it's better to make a single script that pulls field names from the CSV, but since it's a one time operation it isn't really worth the effort.