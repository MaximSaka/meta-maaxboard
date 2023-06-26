
SUMMARY = "The Cython compiler for writing C extensions for the Python language."
HOMEPAGE = "http://cython.org/"
AUTHOR = "Robert Bradshaw, Stefan Behnel, Dag Seljebotn, Greg Ewing, et al. <cython-devel@python.org>"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=e23fadd6ceef8c618fc1c65191d846fa"

SRC_URI = "https://files.pythonhosted.org/packages/da/a0/298340fb8412574a0b00a0d9856aa27e7038da429b9e31d6825173d1e6bd/Cython-0.29.35.tar.gz"
SRC_URI[md5sum] = "138dba31e20e178b431a2e403154f906"
SRC_URI[sha256sum] = "6e381fa0bf08b3c26ec2f616b19ae852c06f5750f4290118bf986b6f85c8c527"

S = "${WORKDIR}/Cython-0.29.35"

RDEPENDS_${PN} = ""

inherit setuptools3
