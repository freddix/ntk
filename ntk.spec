%define		gitver	b371dc0f09c1aa165a8d40339681f9b66305bbc5

Summary:	FLTK fork with additional functionality
Name:		ntk
Version:	1.3.0
Release:	1
License:	LGPL with amendments (see COPYING)
Group:		X11/Libraries
# git://git.tuxfamily.org/gitroot/non/fltk.git
Source0:	%{name}-%{version}-%{gitver}.tar.xz
# Source0-md5:	667d4968c67909db6ec5d2bbc5bbef88
URL:		http://www.fltk.org/
BuildRequires:	cairo-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXft-devel
BuildRequires:	xorg-util-makedepend
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	libntk.*

%description
NTK is a fork of NTK 1.3.0 which adds graphics rendering via
Cairo, support for transparent/overlapping widgets, streamlining
of internals, and some new/improved widgets.

%package devel
Summary:	NTK development files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
NTK development files.

%prep
%setup -q

%{__sed} -i "s|/sbin/ldconfig|/usr/bin/true|g" wscript

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
./waf configure \
	--libdir=%{_libdir}	\
	--prefix=%{_prefix}	\
        --mandir=%{_mandir}	\
	--nocache
./waf -v build

%install
rm -rf $RPM_BUILD_ROOT

./waf -v install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
# note: COPYING contains amendments to LGPL, so don't remove!
%doc COPYING CREDITS README
%attr(755,root,root) %{_bindir}/ntk-chtheme
%attr(755,root,root) %ghost %{_libdir}/libntk.so.1
%attr(755,root,root) %ghost %{_libdir}/libntk_images.so.1
%attr(755,root,root) %{_libdir}/libntk.so.*.*
%attr(755,root,root) %{_libdir}/libntk_images.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ntk-fluid
%attr(755,root,root) %{_libdir}/libntk.so
%attr(755,root,root) %{_libdir}/libntk_images.so
%{_includedir}/ntk
%{_pkgconfigdir}/ntk.pc
%{_pkgconfigdir}/ntk_images.pc

