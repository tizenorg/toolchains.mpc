Name:       mpc
Summary:    A multiprecision library
Version:    0.9
Release:    1
Group:      Development/Libraries
License:    LGPL2.1
URL:        http://www.multiprecision.org/
Source0:    http://www.multiprecision.org/mpc/download/%{name}-%{version}.tar.gz
Source1:    mpc-rpmlintrc
Source1001: packaging/mpc.manifest 
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel


%description
Mpc is a C library for the arithmetic of complex numbers with arbitrarily 
high precision and correct rounding of the result. It is built upon and 
follows the same principles as Mpfr. The library is written by Andreas 
Enge, Philippe Theveny and Paul Zimmermann and is distributed under r the
Gnu Lesser General Public License, either version 2.1 of the licence, or 
(at your option) any later version.



%package devel
Summary:    Development tools for the MPC Library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}, gmp-devel, mpfr-devel

%description devel
The header files, documentation and static libraries for developing
applications using the MPC Library.



%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .
autoreconf --install --force

%configure --disable-static \
    EGREP=egrep


make
%install
rm -rf %{buildroot}

%make_install


%docs_package

%files
%manifest mpc.manifest
%defattr(-,root,root,-)
/usr/lib/libmpc.so
/usr/lib/libmpc.so.2
/usr/lib/libmpc.so.2.0.0


%files devel
%manifest mpc.manifest
%defattr(-,root,root,-)
/usr/include/mpc.h
