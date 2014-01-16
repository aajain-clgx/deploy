#!/user/bin/env/python

"""
Copies a node application source tree to a destination directory
"""

import os
import os.path
from shutil import copytree, ignore_patterns, rmtree
import optparse
import sys

__version__ = '0.1'

def deploy(src_dir, dest_dir, app_name):
  """Deploys the application app_name in src_dir to dest_dir/app_name."""

  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

  path_to_src = os.path.join(src_dir, app_name)
  if not os.path.exists(path_to_src):
    raise IOError('Bad application path: ' + path_to_src)

  path_to_app = os.path.join(dest_dir, app_name)
  if os.path.exists(path_to_app):
    sys.stdout.write('Deleting application ' + app_name + ' in ' + src_dir + ' ... ')
    rmtree(path_to_app)
    print('done')
  else:
    print('No application in ' + src_dir + ' to delete. Free to copy.')

  print('Copying source from ' + path_to_src + ' to ' + path_to_app)
  copytree(path_to_src, path_to_app, ignore=ignore_patterns(
    '.gitignore',
    '.git',
    'LICENSE',
    '*.md',
    '.npmignore',
    '.travis.yml',
    'Jakefile'))

def main():
  """main"""
  option_parser = optparse.OptionParser(
      usage='usage: %prog SRC_DIR DEST_DIR APP_NAME\n' +
        'Deploys application APP_NAME from SRC_DIR to DEST_DIR.',
      version='%prog ' + __version__
  )
  (options, args) = option_parser.parse_args()
  if not (len(args) == 3):
    option_parser.error('Incorrect number of program arguments')
  deploy(args[0], args[1], args[2])

if __name__ == "__main__":
  sys.exit(main())
