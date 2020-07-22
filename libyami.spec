Name:                libyami
Version:             1.3.1
Release:             3
Summary:             Another Media Infrastructure
License:             ASL 2.0 and BSD
URL:                 https://github.com/intel/libyami
Source0:             https://github.com/intel/libyami/archive/fb48083de91f837ddbf599dd4b5ad1eb1239e1cf/libyami-fb48083.tar.gz 
Patch0000:           libyami-libtool-macro.patch
BuildRequires:       libtool gcc-c++ libva-devel pkgconfig(libdrm) pkgconfig(x11)
%description
Yami is the core building block of a media solution. It uses hardware acceleration to parses and decode video streams.

%package             devel
Summary:             Development files for libyami
Requires:            libyami = %{version}-%{release}
%description         devel
Libyami-devel package contains libraries and header files used
for developing applications using libyami.

%prep
%autosetup -n libyami-fb48083de91f837ddbf599dd4b5ad1eb1239e1cf -p1
autoreconf -vif

%build
%configure --disable-static --enable-dmabuf --enable-wayland \
           --enable-mpeg2dec --enable-vp9dec --enable-vc1dec \
           --enable-fakedec --enable-jpegenc --enable-vp8svct \
           --enable-vp9enc --enable-h265enc
%make_build V=1

%install
%make_install
%delete_la

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%files
%doc NEWS README.md codecparsers/{dboolhuff.LICENSE,vp9quant.LICENSE} LICENSE.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libyami.pc

%changelog
* Thu Jun 11 2020 wangchong <wangchong56@huawei.com> - 1.3.1-3
- package init
