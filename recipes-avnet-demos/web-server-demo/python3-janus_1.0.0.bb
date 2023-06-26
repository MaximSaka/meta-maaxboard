
SUMMARY = "Mixed sync-async queue to interoperate between asyncio tasks and classic threads"
HOMEPAGE = "https://github.com/aio-libs/janus"
AUTHOR = "Andrew Svetlov <andrew.svetlov@gmail.com> <andrew.svetlov@gmail.com>"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=23878c357ebb4c8ce1109be365043349"

SRC_URI = "https://files.pythonhosted.org/packages/b8/a8/facab7275d7d3d2032f375843fe46fad1cfa604a108b5a238638d4615bdc/janus-1.0.0.tar.gz"
SRC_URI[md5sum] = "2d8c0b884c14f18fc5223858eb16461e"
SRC_URI[sha256sum] = "df976f2cdcfb034b147a2d51edfc34ff6bfb12d4e2643d3ad0e10de058cb1612"

S = "${WORKDIR}/janus-1.0.0"

RDEPENDS_${PN} = "python3-typing-extensions"

inherit setuptools3
