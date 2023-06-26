
SUMMARY = "A common runtime for AWS Python projects"
HOMEPAGE = "https://github.com/awslabs/aws-crt-python"
AUTHOR = "Amazon Web Services, Inc <aws-sdk-common-runtime@amazon.com>"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE;md5=3b83ef96387f14655fc854ddc3c6bd57"

SRC_URI = "https://files.pythonhosted.org/packages/1f/34/5392a41ab94f9723bee647f7757bd79a75da657137f3b1f0128a8f9ba6ad/awscrt-0.16.21.tar.gz"
SRC_URI[md5sum] = "4f7123c461f4c482860ec8f1d1b00f89"
SRC_URI[sha256sum] = "263cbaf16dc970d0807bd3208323f251728072076c08ec1fe1235a2683dbe1f4"

S = "${WORKDIR}/awscrt-0.16.21"

RDEPENDS_${PN} = ""

inherit setuptools3
