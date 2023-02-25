# Can not find libraries for some reason
%global debug_package %{nil}

Name:           glewmx
Version:        1.13.0
Release:        %autorelease
Summary:        OpenGL Extension Wrangler MX

License:        GPLv3+
URL:            https://launchpad.net/ubuntu/+source/glewmx
Source0:        http://archive.ubuntu.com/ubuntu/pool/universe/g/glewmx/glewmx_%{version}.orig.tar.gz
Source1:        http://archive.ubuntu.com/ubuntu/pool/universe/g/glewmx/glewmx_%{version}-5.debian.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: mesa-libGLU-devel
BuildRequires: pkgconfig(glu)
BuildRequires: libXmu-devel
BuildRequires: libXi-devel

%description
OpenGL Extension Wrangler MX. The MX version is discountinued but is maintained in Ubuntu.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n glew-%{version}
tar -x -I 'xz -d -T0 -k' -f '%{SOURCE1}'

for i in debian/patches/*.patch; do patch -p1 < $i; done
sed -i 's:$(GLEW_DEST)/include/GL:$(GLEW_DEST)/include/glewmx-%{version}/GL:' Makefile

%build
# This doesn't get actually installed but is to change glewmx.pc before installation
%make_build
sed -i 's:includedir=${prefix}/include:includedir=${prefix}/include/glewmx-%{version}:' glewmx.pc

%install
# Only MX is installed
%make_build DESTDIR=%{buildroot} INSTALL="/usr/bin/install -p" install.mx

%files
%license LICENSE.txt
%{_libdir}/libGLEWmx.so.*

%files devel
%dir %{_includedir}/glewmx-%version
%dir %{_includedir}/glewmx-%version/GL
%{_includedir}/glewmx-%version/GL/*.h
%{_libdir}/libGLEWmx.a
%{_libdir}/libGLEWmx.so
%{_libdir}/pkgconfig/glewmx.pc

%changelog
%autochangelog
