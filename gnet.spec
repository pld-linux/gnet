# Note that this is NOT a relocatable package
%define ver      1.0.1
%define rel      1
%define prefix   /usr

Summary: Gnet, a network library
Name:      gnet
Version:   %ver
Release:   %rel
Copyright: LGPL
Group: Libraries/Network
Source0:   gnet-%{PACKAGE_VERSION}.tar.gz
URL:       http://www.eecs.umich.edu/~dhelder/misc/gnet
BuildRoot: /var/tmp/gnet-%{PACKAGE_VERSION}-root
Docdir: %{prefix}/doc
Packager: Xavier Nicolovici <nicolovi@club-internet.fr>
Requires: glib >= 1.2

%description
Gnet is a simple network library.  It is writen in C, object-oriented,
and built upon glib.  It is intended to be small, fast, easy-to-use,
and easy to port.  The interface is similar to the interface for
Java's network library.

Features:
  * TCP 'client' sockets
  * TCP 'server' sockets
  * Non-blocking TCP sockets
  * UDP
  * IP Multicast
  * Internet address abstraction

Gnet requires Glib 1.2.  You can get this at www.gtk.org.  Or, if you
have a system with packages (eg, Red Hat or Debian), look for the
latest glib package.

Comments, questions, and bug reports should be sent to
gnet-dev@eecs.umich.edu.

The Gnet homepage is at http://www.eecs.umich.edu/~dhelder/misc/gnet

%package devel
Summary: Header files for the Gnet library
Group: Development/Libraries

%description devel
Gnet is a simple network library.  It is writen in C, object-oriented,
and built upon glib.
This package allows you to develop applications that use the Gnet
library.


%prep
%setup

%build
%ifarch alpha
   CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" ./configure --host=alpha-redhat-linux\
	--prefix=%{prefix} \
	--enable-debug=yes \
	--with-gnu-ld
%else
   CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" ./configure \
	--prefix=%{prefix} \
	--enable-debug=yes \
	--with-gnu-ld 
%endif
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc README COPYING ChangeLog NEWS TODO AUTHORS INSTALL HACKING
%{prefix}/bin/gnet-config
%{prefix}/share/aclocal/gnet.m4
%doc doc/html
%{prefix}/lib/libgnet-1.0.so.*

%files devel
%defattr(-, root, root)
%{prefix}/include/gnet
%{prefix}/lib/*a
%{prefix}/lib/lib*.so

%changelog
* Mon Feb 28 2000 David Helder <dhelder@umich.edu>
- Updated for version 1.0

* Sat Jan 15 2000 Xavier Nicolovici <nicolovi@club-internet.fr>
- Moved lib*.so and lib*a to the devel package
- Creation of a gnet.spec.in for autoconf process

* Wed Jan 14 2000 Xavier Nicolovici <nicolovi@club-internet.fr>
- HTML documentation has been move to /usr/doc/gnet-{version}/html

* Thu Jan 13 2000 Xavier Nicolovici <nicolovi@club-internet.fr>
- First try at an RPM
