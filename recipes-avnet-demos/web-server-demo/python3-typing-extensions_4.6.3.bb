
SUMMARY = "Backported and Experimental Type Hints for Python 3.7+"
HOMEPAGE = ""
AUTHOR = " <"Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com>>"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=fcf6b249c2641540219a727f35d8d2c2"

SRC_URI = "https://files.pythonhosted.org/packages/42/56/cfaa7a5281734dadc842f3a22e50447c675a1c5a5b9f6ad8a07b467bffe7/typing_extensions-4.6.3.tar.gz"
SRC_URI[md5sum] = "111a7d37292a241811502bd1b64032be"
SRC_URI[sha256sum] = "d91d5919357fe7f681a9f2b5b4cb2a5f1ef0a1e9f59c4d8ff0d3491e05c0ffd5"

S = "${WORKDIR}/typing_extensions-4.6.3"

RDEPENDS_${PN} = ""

inherit setuptools3
