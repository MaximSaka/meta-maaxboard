
SUMMARY = "MQTT version 5.0/3.1.1 client class"
HOMEPAGE = "http://eclipse.org/paho"
AUTHOR = "Roger Light <roger@atchoo.org>"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=8e5f264c6988aec56808a3a11e77b913"

SRC_URI = "https://files.pythonhosted.org/packages/f8/dd/4b75dcba025f8647bc9862ac17299e0d7d12d3beadbf026d8c8d74215c12/paho-mqtt-1.6.1.tar.gz"
SRC_URI[md5sum] = "bdb20f88db291fdb4a0fe804c0f29316"
SRC_URI[sha256sum] = "2a8291c81623aec00372b5a85558a372c747cbca8e9934dfe218638b8eefc26f"

S = "${WORKDIR}/paho-mqtt-1.6.1"

RDEPENDS_${PN} = ""

inherit setuptools3
