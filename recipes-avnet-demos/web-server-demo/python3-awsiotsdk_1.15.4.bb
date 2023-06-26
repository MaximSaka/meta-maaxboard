
SUMMARY = "AWS IoT SDK based on the AWS Common Runtime"
HOMEPAGE = "https://github.com/aws/aws-iot-device-sdk-python-v2"
AUTHOR = "AWS SDK Common Runtime Team <>"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://setup.py;md5=e35b3fc5227a71304a183fa9c421aaae"

SRC_URI = "https://files.pythonhosted.org/packages/00/df/b9c665be9b2b2c9e2971907079ca4e66c73026a4a2576c808d9e77b8574b/awsiotsdk-1.15.4.tar.gz"
SRC_URI[md5sum] = "ae768dda733893a319bbac90fe65df02"
SRC_URI[sha256sum] = "51126c00ce15c0b53b41ce07409484896ce2545ca770cde7cda647b73ce50a34"

S = "${WORKDIR}/awsiotsdk-1.15.4"

RDEPENDS_${PN} = "python3-awscrt"

inherit setuptools3
