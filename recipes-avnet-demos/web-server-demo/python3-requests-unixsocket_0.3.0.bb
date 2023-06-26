
SUMMARY = "Use requests to talk HTTP via a UNIX domain socket"
HOMEPAGE = "https://github.com/msabramo/requests-unixsocket"
AUTHOR = "Marc Abramowitz <marc@marc-abramowitz.com>"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=d2794c0df5b907fdace235a619d80314"

SRC_URI = "https://files.pythonhosted.org/packages/c3/ea/0fb87f844d8a35ff0dcc8b941e1a9ffc9eb46588ac9e4267b9d9804354eb/requests-unixsocket-0.3.0.tar.gz"
SRC_URI[md5sum] = "2da31f8d76fb563bc3fd6d59a2fb260a"
SRC_URI[sha256sum] = "28304283ea9357d45fff58ad5b11e47708cfbf5806817aa59b2a363228ee971e"

S = "${WORKDIR}/requests-unixsocket-0.3.0"

RDEPENDS_${PN} = "python3-requests"

inherit setuptools3
