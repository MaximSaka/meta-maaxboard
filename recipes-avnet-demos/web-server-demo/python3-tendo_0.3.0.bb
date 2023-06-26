
SUMMARY = "A Python library that extends some core functionality"
HOMEPAGE = "https://github.com/pycontribs/tendo"
AUTHOR = "Sorin Sbarnea <sorin.sbarnea@gmail.com>"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=b51670bf5aec65207814a2ad228fa55a"

SRC_URI = "https://files.pythonhosted.org/packages/b9/a1/714b2bee108ccfdc160d74ca81459feb8d08753921200637f890eab79545/tendo-0.3.0.tar.gz"
SRC_URI[md5sum] = "7266b0b1dc4f537d25caf03f9cc1d698"
SRC_URI[sha256sum] = "68392d686eb6ece71c14ff0fe24340e83c4362525c8b26f144c84f3122ae9e77"

S = "${WORKDIR}/tendo-0.3.0"

RDEPENDS_${PN} = "python3-six"

inherit setuptools3
