# Currently, this makefiles erases the .bz2 files when there is a crash, making the 
# build longer than necessary when you restart.

PKGVERSION=2010.11.09

all: ubuntu-keyring-${PKGVERSION}-pr2_all.deb

nobuild: work/ubuntu-keyring-${PKGVERSION}-pr2

clean:
	rm -rf work

work:
	mkdir work

work/ubuntu-keyring-${PKGVERSION}: work
	cd work; apt-get source ubuntu-keyring=${PKGVERSION}

work/ubuntu-keyring-${PKGVERSION}-pr2: work/ubuntu-keyring-${PKGVERSION}
	cp -r work/ubuntu-keyring-${PKGVERSION} work/ubuntu-keyring-${PKGVERSION}-pr2
	cd work/ubuntu-keyring-${PKGVERSION}-pr2; patch -p1 < ../../ubuntu-keyring_${PKGVERSION}-pr2.diff

ubuntu-keyring-${PKGVERSION}-pr2_all.deb: work/ubuntu-keyring-${PKGVERSION}-pr2
	cd work/ubuntu-keyring-${PKGVERSION}-pr2; dpkg-buildpackage -uc -b; fakeroot debian/rules clean; cd ..

