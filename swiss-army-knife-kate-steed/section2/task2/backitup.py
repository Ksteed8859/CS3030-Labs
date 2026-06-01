import shutil
from datetime import date

archive_date = date.today().strftime("%Y-%m-%d")
shutil.make_archive(archive_date, 'zip', '../../section1', '../..', 'section1')