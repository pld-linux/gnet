Summary:	Gnet, a network library
Name:		gnet
Version:	1.0.1
Release:	1
License:	LGPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.eecs.umich.edu/~dhelder/misc/gnet/src/%{name}-%{version}.tar.gz
URL:		http://www.eecs.umich.edu/~dhelder/misc/gnet/
BuildRequires:	glib-devel >= 1.2
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_aclocaldir	%(aclocal --print-ac-dir)

%description
Gnet is a simple network library. It is writen in C, object-oriented, and
built upon glib. It is intended to be small, fast, easy-to-use, and easy
to port. The interface is similar to the interface for Java's network
library. Features:
   * TCP 'client' sockets
   * TCP 'server' sockets
   * Non-blocking TCP sockets
   * UDP
   * IP Multicast
   * Internet address abstraction

%package devel
Summary:	Header files for the Gnet library
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Gnet is a simple network library. It is writen in C, object-oriented, and
built upon glib. This package allows you to develop applications that use
the Gnet library.

%package static
Summary:	Static Gnet library
Summary(pl):	Biblioteka statyczna Gnet
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static Gnet library.

%description -l pl static
Biblioteka statyczna Gnet.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT
	m4datadir=%{_aclocaldir}

strip --stri-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf README ChangeLog NEWS TODO AUTHORS HACKING

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%doc doc/html
%attr(755,root,root) %{_bindir}/gnet-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_aclocaldir}/gnet.m4
%{_includedir}/gnet

%files static
%attr(644,root,root) %{_libdir}/lib*.a
