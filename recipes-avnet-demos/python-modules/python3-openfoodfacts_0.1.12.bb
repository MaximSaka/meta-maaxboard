
SUMMARY = "Official Python SDK of Open Food Facts"
HOMEPAGE = ""
AUTHOR = "The Open Food Facts team <>"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE;md5=3a6417fee5e655008a3dc4dc9defc9b9"

SRC_URI = "https://files.pythonhosted.org/packages/84/43/c8d3e8c4c3871b83f083aa31246d9cfc8d661d020d12fb246d3e8738eb24/openfoodfacts-0.1.12.tar.gz"
SRC_URI[md5sum] = "fe3f783da6500b27a9b1e53e5c54d0c6"
SRC_URI[sha256sum] = "8b7aed312c66d470e7a9083b2f6afe7afbe26bd1aaaaa4bbfb4878c61bf28022"

S = "${WORKDIR}/openfoodfacts-0.1.12"

RDEPENDS_${PN} = "python3-requests python3-pydantic python3-tqdm"

inherit pypi python_poetry_core
