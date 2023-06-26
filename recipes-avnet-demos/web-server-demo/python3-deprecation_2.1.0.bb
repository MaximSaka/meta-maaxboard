
SUMMARY = "A library to handle automated deprecations"
HOMEPAGE = "http://deprecation.readthedocs.io/"
AUTHOR = "Brian Curtin <brian@python.org>"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=e3fc50a88d0a364313df4b21ef20c29e"

SRC_URI = "https://files.pythonhosted.org/packages/5a/d3/8ae2869247df154b64c1884d7346d412fed0c49df84db635aab2d1c40e62/deprecation-2.1.0.tar.gz"
SRC_URI[md5sum] = "6b79c6572fb241e3cecbbd7d539bb66b"
SRC_URI[sha256sum] = "72b3bde64e5d778694b0cf68178aed03d15e15477116add3fb773e581f9518ff"

S = "${WORKDIR}/deprecation-2.1.0"

RDEPENDS_${PN} = "python3-packaging"

inherit setuptools3
