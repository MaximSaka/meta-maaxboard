
SUMMARY = "Copy open-food-facts demo to /home/root"
DESCRIPTION = "This recipe copies the contents of the open-food-facts to the /home/root directory on the target system."
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://open-food-facts"

do_install() {
    install -d ${D}/home/root/open-food-facts
    cp -r ${WORKDIR}/open-food-facts ${D}/home/root
    chmod -R a+rX ${D}/home/root/open-food-facts
    chmod +x ${D}/home/root/open-food-facts/update-autolaunch.sh 
}
FILES:${PN} += "/home/root/open-food-facts"
