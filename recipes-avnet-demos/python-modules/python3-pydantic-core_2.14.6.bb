SUMMARY = "Provides the core functionality for pydantic validation and serialization."
DESCRIPTION = "This package provides the core functionality for \
pydantic validation and serialization.\
\
Pydantic-core is currently around 17x faster than pydantic V1."
HOMEPAGE = "https://github.com/pydantic/pydantic-core"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=ab599c188b4a314d2856b3a55030c75c"

SRC_URI = "https://files.pythonhosted.org/packages/b2/7d/8304d8471cfe4288f95a3065ebda56f9790d087edc356ad5bd83c89e2d79/pydantic_core-2.14.6.tar.gz"
SRC_URI[sha256sum] = "1fd0c1d395372843fba13a51c28e3bb9d59bd7aebfeb17358ffaaa1e4dbbe948"

DEPENDS = "python3-typing-extensions"

inherit setuptools3

S = "${WORKDIR}/pydantic_core-${PV}"

PYPI_ARCHIVE_NAME = "pydantic_core-${PV}.${PYPI_PACKAGE_EXT}"

RDEPENDS:${PN} += "python3-typing-extensions"

do_configure:prepend() {
cat > ${S}/setup.py <<-EOF
from setuptools import setup

setup(
       name="pydantic_core",
       version="${PV}",
       license="${LICENSE}",
       description="${DESCRIPTION}",
       long_description="${S}/README.md"
)
EOF
}