Summary:	Gnet, a network library
Summary(pl.UTF-8):	Biblioteka sieciowa
Name:		gnet
Version:	2.0.8
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnet/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	93327d2fca333d7e54ba2cf54e071165
Patch0:		%{name}-nolibs.patch
URL:		http://gnetlibrary.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
#BuildRequires:	gtk-doc
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

%description -l pl.UTF-8
Gnet jest prostą biblioteką sieciową. Jest napisana w C, zorientowana
obiektowo i zbudowana na bazie glib. W zamierzeniu ma być mala,
szybka, łatwa w użyciu i łatwa do przeniesienia na inne systemy.
Interfejs jest podobny do biblioteki sieciowej Javy. Możliwości to:
   - gniazda 'klienckie' TCP
   - gniazda 'serwerowe' TCP
   - nie-blokujące gniazda TCP
   - UDP
   - IP Multicast

%package devel
Summary:	Header files for the Gnet library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki Gnet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0
Requires:	gtk-doc-common

%description devel
Gnet is a simple network library. It is writen in C, object-oriented,
and built upon glib. This package allows you to develop applications
that use the Gnet library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki Gnet.

%package static
Summary:	Static Gnet library
Summary(pl.UTF-8):	Biblioteka statyczna Gnet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Gnet library.

%description static -l pl.UTF-8
Biblioteka statyczna Gnet.

%prep
%setup -q
%patch0 -p1

# don't BR glib-devel
echo -e 'AC_DEFUN([AM_PATH_GLIB], [$3\n:])' >> acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gtk-doc \
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
%ghost %attr(755,root,root) %{_libdir}/lib*.so.?

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
