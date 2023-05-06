Name:                libyami
Version:             1.3.2
Release:             2
Summary:             Another Media Infrastructure
License:             ASL 2.0 and BSD
URL:                 https://github.com/intel/libyami
Source0:             https://github.com/intel/libyami/archive/%{version}/%{name}-%{version}.tar.gz
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
%autosetup -n %{name}-%{version} -p1
autoreconf -vif

%build
%if "%toolchain" == "clang"
	export CXXFLAGS="$CXXFLAGS -Wno-unused-function -Wno-unused-const-variable -Wno-overloaded-virtual -Wno-tautological-constant-out-of-range-compare"
%endif
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
* Sat May 06 2023 yoo <sunyuechi@iscas.ac.cn> - 1.3.2-2
- fix clang build error

* Tue Jun 29 2021 lingsheng <lingsheng@huawei.com> - 1.3.2-1
- Update to 1.3.2

* Thu Jun 11 2020 wangchong <wangchong56@huawei.com> - 1.3.1-3
- package init
