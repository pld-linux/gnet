Summary:	Gnet, a network library
Summary(pl):	Biblioteka sieciowa
Name:		gnet
Version:	2.0.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.gnetlibrary.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	b43e728391143214e2cfd0b835b6fd2a
Patch0:		%{name}-nolibs.patch
URL:		http://gnetlibrary.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnet is a simple network library. It is writen in C, object-oriented,
and built upon glib. It is intended to be small, fast, easy-to-use,
and easy to port. The interface is similar to the interface for Java's
network library. Features:
   - TCP 'client' sockets
   - TCP 'server' sockets
   - Non-blocking TCP sockets
   - UDP
   - IP Multicast
   - Internet address abstraction

%description -l pl
Gnet jest prost± bibliotek± sieciow±. Jest napisana w C, zorientowana
objektowo i zbudowana na bazie glib. W zamierzeniu ma byæ mala,
szybka, ³atwa w u¿yciu i ³atwa do przeniesienia na inne systemy.
Interfejs jest podobny do biblioteki sieciowej Javy. Mo¿liwo¶ci to:
   - gniazda 'klienckie' TCP
   - gniazda 'serwerowe' TCP
   - nie-blokuj±ce gniazda TCP
   - UDP
   - IP Multicast

%package devel
Summary:	Header files for the Gnet library
Summary(pl):	Pliki nag³ówkowe dla biblioteki Gnet
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel
Requires:	gtk-doc-common

%description devel
Gnet is a simple network library. It is writen in C, object-oriented,
and built upon glib. This package allows you to develop applications
that use the Gnet library.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki Gnet.

%package static
Summary:	Static Gnet library
Summary(pl):	Biblioteka statyczna Gnet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Gnet library.

%description static -l pl
Biblioteka statyczna Gnet.

%prep
%setup -q
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_libdir}/gnet-2.0
%{_includedir}/gnet-2.0
%{_aclocaldir}/gnet-2.0.m4
%{_pkgconfigdir}/gnet-2.0.pc
%{_gtkdocdir}/gnet

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
