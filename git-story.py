#!/usr/bin/env python

import sh

"""
This command can show much better log, and try to write git commit as a story.

##### Reference

- [Your Git Log Should Tell A Story](http://www.mokacoding.com/blog/your-git-log-should-tell-a-story/?utm_campaign=CodeTengu&utm_medium=web&utm_source=CodeTengu_75)

"""

print(sh.git.log("--format=oneline", "--abbrev-commit"))
