# BEGIN: Copyright 
# Copyright (C) 2019 Rector and Visitors of the University of Virginia 
# All rights reserved 
# END: Copyright 

# BEGIN: License 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
#   http://www.apache.org/licenses/LICENSE-2.0 
# END: License 

import re


class Status(object):
    def __init__(self, status):
        self.state = status[0]
        self.is_modified = status[1] == 'M'

        if self.is_renamed or self.is_copied:
            matches = re.search(r'(\S+?)\s+->\s+(\S+?)$', status[3:])
            self.original_path = matches.groups()[0]
            self.path = matches.groups()[1]
        else:
            self.path = status[3:]

    def __str__(self):
        status = '{:1}{:1}'.format(self.state, 'M' if self.is_modified else '')
        if self.is_renamed or self.is_copied:
            status = '{:3}{} -> {}'.format(status, self.original_path, self.path)
        else:
            status = '{:3}{}'.format(status, self.path)
        return status

    def __repr__(self):  # pragma: no cover
        return '<Status {}>'.format(self.path)

    @property
    def is_staged(self):
        """If the state is empty then the file is unstaged."""
        return self.state not in (' ', '?',)

    @property
    def is_untracked(self):
        """Returns true if the file is untracked."""
        return self.state == '?'

    @property
    def is_renamed(self):
        """Returns true if the file is renamed."""
        return self.state == 'R'

    @property
    def is_copied(self):
        """Returns true if the file is copied."""
        return self.state == 'C'

    @property
    def is_deleted(self):
        """Returns true if the file is deleted."""
        return self.state == 'D'

    @property
    def is_added(self):
        """Returns true if the file is added."""
        return self.state == 'A'
