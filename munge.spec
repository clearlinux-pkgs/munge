#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : munge
Version  : 0.5.13
Release  : 13
URL      : https://github.com//dun/munge/archive/munge-0.5.13.tar.gz
Source0  : https://github.com//dun/munge/archive/munge-0.5.13.tar.gz
Summary  : MUNGE authentication service library
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-3.0 LGPL-3.0+
Requires: munge-bin = %{version}-%{release}
Requires: munge-config = %{version}-%{release}
Requires: munge-lib = %{version}-%{release}
Requires: munge-license = %{version}-%{release}
Requires: munge-man = %{version}-%{release}
Requires: munge-services = %{version}-%{release}
BuildRequires : bzip2-dev
BuildRequires : libgcrypt-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(zlib)
Patch1: munge-service.patch
Patch2: munge-conf.patch

%description
MUNGE (MUNGE Uid 'N' Gid Emporium) is an authentication service for creating
and validating credentials.  It is designed to be highly scalable for use
in an HPC cluster environment.  It allows a process to authenticate the
UID and GID of another local or remote process within a group of hosts
having common users and groups.  These hosts form a security realm that is
defined by a shared cryptographic key.  Clients within this security realm
can create and validate credentials without the use of root privileges,
reserved ports, or platform-specific methods.

%package bin
Summary: bin components for the munge package.
Group: Binaries
Requires: munge-config = %{version}-%{release}
Requires: munge-license = %{version}-%{release}
Requires: munge-services = %{version}-%{release}

%description bin
bin components for the munge package.


%package config
Summary: config components for the munge package.
Group: Default

%description config
config components for the munge package.


%package dev
Summary: dev components for the munge package.
Group: Development
Requires: munge-lib = %{version}-%{release}
Requires: munge-bin = %{version}-%{release}
Provides: munge-devel = %{version}-%{release}
Requires: munge = %{version}-%{release}

%description dev
dev components for the munge package.


%package lib
Summary: lib components for the munge package.
Group: Libraries
Requires: munge-license = %{version}-%{release}

%description lib
lib components for the munge package.


%package license
Summary: license components for the munge package.
Group: Default

%description license
license components for the munge package.


%package man
Summary: man components for the munge package.
Group: Default

%description man
man components for the munge package.


%package services
Summary: services components for the munge package.
Group: Systemd services

%description services
services components for the munge package.


%prep
%setup -q -n munge-munge-0.5.13
cd %{_builddir}/munge-munge-0.5.13
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576089597
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --with-crypto-lib=openssl
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1576089597
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/munge
cp %{_builddir}/munge-munge-0.5.13/COPYING %{buildroot}/usr/share/package-licenses/munge/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/munge-munge-0.5.13/COPYING.LESSER %{buildroot}/usr/share/package-licenses/munge/e203d4ef09d404fa5c03cf6590e44231665be689
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/munge
/usr/bin/munged
/usr/bin/remunge
/usr/bin/unmunge

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/munge.conf

%files dev
%defattr(-,root,root,-)
/usr/include/munge.h
/usr/lib64/libmunge.so
/usr/lib64/pkgconfig/munge.pc
/usr/share/man/man3/munge.3
/usr/share/man/man3/munge_ctx.3
/usr/share/man/man3/munge_ctx_copy.3
/usr/share/man/man3/munge_ctx_create.3
/usr/share/man/man3/munge_ctx_destroy.3
/usr/share/man/man3/munge_ctx_get.3
/usr/share/man/man3/munge_ctx_set.3
/usr/share/man/man3/munge_ctx_strerror.3
/usr/share/man/man3/munge_decode.3
/usr/share/man/man3/munge_encode.3
/usr/share/man/man3/munge_enum.3
/usr/share/man/man3/munge_enum_int_to_str.3
/usr/share/man/man3/munge_enum_is_valid.3
/usr/share/man/man3/munge_enum_str_to_int.3
/usr/share/man/man3/munge_strerror.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmunge.so.2
/usr/lib64/libmunge.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/munge/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/munge/e203d4ef09d404fa5c03cf6590e44231665be689

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/munge.1
/usr/share/man/man1/remunge.1
/usr/share/man/man1/unmunge.1
/usr/share/man/man7/munge.7
/usr/share/man/man8/munged.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/munge.service