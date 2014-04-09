Kerberos enabled Jenkins job configuration manipulator :-)

HOW-TO
======
 * Take a look into properties.py and sf_downloader.py
 * Run sf_downloader.py
  * e.g. ```python src/sf_downloader.py '^(?!.*noe).*$'``` will download all jobs but those with ```noe``` in their name.
 * Make any additional XML transformations you like
 * Run sf_uploader.py
 
Footnote
--------
 * I have updated dozens of jobs with this tool, however, use at your own risk...
 * Some python libs, available as rpms, you will need:
   * python-lxml
   * python-kerberos
   * python-urllib2_kerberos

