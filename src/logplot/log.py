from collections import namedtuple

LogEntry = namedtuple("LogEntry", ["line_number", "conf_entry", "timestamp"])
LogEntry.__new__.__defaults__ = (None,)  # timestamp is optional


def parse(path, conf):
    entries, special_entries = [], []
    with open(path) as f:
        for number, line in enumerate(f, 1):
            for entry in conf.entries:
                if entry.identifier in line:
                    entries.append(LogEntry(line_number=number, conf_entry=entry))
            for special_entry in conf.special_entries:
                if special_entry.identifier in line:
                    special_entries.append(
                        LogEntry(line_number=number, conf_entry=special_entry)
                    )
    return entries, special_entries
