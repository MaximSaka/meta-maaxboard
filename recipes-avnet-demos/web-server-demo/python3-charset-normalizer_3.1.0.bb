
SUMMARY = "The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet."
HOMEPAGE = "https://github.com/Ousret/charset_normalizer"
AUTHOR = "Ahmed TAHRI <ahmed.tahri@cloudnursery.dev>"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=0974a390827087287db39928f7c524b5"

SRC_URI = "https://files.pythonhosted.org/packages/ff/d7/8d757f8bd45be079d76309248845a04f09619a7b17d6dfc8c9ff6433cac2/charset-normalizer-3.1.0.tar.gz"
SRC_URI[md5sum] = "1c425218e80cd77b375ce6c50317dc56"
SRC_URI[sha256sum] = "34e0a2f9c370eb95597aae63bf85eb5e96826d81e3dcf88b8886012906f509b5"

S = "${WORKDIR}/charset-normalizer-3.1.0"

RDEPENDS_${PN} = ""

inherit setuptools3
