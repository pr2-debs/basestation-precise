# Currently, this makefiles erases the .bz2 files when there is a crash, making the 
# build longer than necessary when you restart.

PKGVERSION=2011.11.21.1

all: ubuntu-keyring-${PKGVERSION}-pr2_all.deb

nobuild: work/ubuntu-keyring-${PKGVERSION}-pr2

clean:
	rm -rf work
	rm -rf ros.key pr2.key pr2-packages.key

work:
	mkdir work

work/ubuntu-keyring-${PKGVERSION}: work
	cd work; apt-get source ubuntu-keyring=${PKGVERSION}

ros.key:
	wget http://packages.ros.org/ros.key

pr2.key:
	wget http://packages.ros.org/pr2.key
	
pr2-packages.key: ../../basestation-precise/pr2-installer/root/usr/lib/robot-install/pr2-packages.key
	cp ../../basestation-precise/pr2-installer/root/usr/lib/robot-install/pr2-packages.key .

#basestationpackages.key: ../../basestation-precise/pr2-installer/root/usr/lib/robot-install/basestationpackages.gpg
#	gpg --no-default-keyring --secret-keyring ./$< --export -a 324C3C1E | tee $@

keys: ros.key pr2-packages.key basestationpackages.key

work/ubuntu-keyring-${PKGVERSION}-pr2: work/ubuntu-keyring-${PKGVERSION} keys
	cp -r work/ubuntu-keyring-${PKGVERSION} work/ubuntu-keyring-${PKGVERSION}-pr2
	cd work/ubuntu-keyring-${PKGVERSION}-pr2; patch -p1 < ../../ubuntu-keyring_${PKGVERSION}-pr2.diff
	gpg --no-default-keyring --keyring work/ubuntu-keyring-${PKGVERSION}-pr2/keyrings/ubuntu-archive-keyring.gpg --import ros.key
	gpg --no-default-keyring --keyring work/ubuntu-keyring-${PKGVERSION}-pr2/keyrings/ubuntu-archive-keyring.gpg --import pr2-packages.key
	gpg --no-default-keyring --keyring work/ubuntu-keyring-${PKGVERSION}-pr2/keyrings/ubuntu-archive-keyring.gpg --import basestationpackages.key
	rm -r work/ubuntu-keyring-${PKGVERSION}-pr2/keyrings/ubuntu-archive-keyring.gpg~

ubuntu-keyring-${PKGVERSION}-pr2_all.deb: work/ubuntu-keyring-${PKGVERSION}-pr2
	cd work/ubuntu-keyring-${PKGVERSION}-pr2; dpkg-buildpackage -uc -b; fakeroot debian/rules clean; cd ..

