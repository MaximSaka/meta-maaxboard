
SUMMARY = "A Python SOCKS client module. See https://github.com/Anorov/PySocks for more information."
HOMEPAGE = "https://github.com/Anorov/PySocks"
AUTHOR = "Anorov <anorov.vorona@gmail.com>"
LICENSE = "BSD"
LIC_FILES_CHKSUM = "file://LICENSE;md5=1d457bcffb9661b45f799d4efee72f16"

SRC_URI = "https://files.pythonhosted.org/packages/bd/11/293dd436aea955d45fc4e8a35b6ae7270f5b8e00b53cf6c024c83b657a11/PySocks-1.7.1.tar.gz"
SRC_URI[md5sum] = "89b1a6865c61bae67a32417517612ee6"
SRC_URI[sha256sum] = "3f8804571ebe159c380ac6de37643bb4685970655d3bba243530d6558b799aa0"

S = "${WORKDIR}/PySocks-1.7.1"

RDEPENDS_${PN} = ""

inherit setuptools3
