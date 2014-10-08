
SVN=pr2_force_torque_calibration
SVN_URL=https://code.ros.org/svn/wg-ros-pkg/pr2_mods/pr2_force_torque_calibration
REV=55338

all: ${SVN}
.PHONY: all

${SVN}:
	svn co -r ${REV} ${SVN_URL}

install-dirs:
	mkdir -p ${DESTDIR}/usr/share/pr2-ft
	mkdir -p ${DESTDIR}/usr/bin

install: ${SVN}
	install pr2-ft-config ${DESTDIR}/usr/bin/
	find ${DESTDIR}
	rsync -a --exclude='.svn' ${SVN}/ ${DESTDIR}/usr/share/pr2-ft

clean:
	-rm -rf ${SVN}
