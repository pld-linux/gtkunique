Summary:	Library to make sure only one instance of a program is running
Summary(pl.UTF-8):	Biblioteka zapewniająca uruchamianie tylko jednej instancji programu
Name:		gtkunique
Version:	0.9.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	ba00da4858cadb132948840a235454d8
URL:		http://svn.gnome.org/viewcvs/gtkunique/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to make sure only one instance of a program is running.

%description -l pl.UTF-8
Biblioteka zapewniająca uruchamianie tylko jednej instancji programu.

%package devel
Summary:	Header files for gtkunique library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gtkunique
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gtkunique library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtkunique.

%package static
Summary:	Static gtkunique library
Summary(pl.UTF-8):	Statyczna biblioteka gtkunique
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtkunique library.

%description static -l pl.UTF-8
Statyczna biblioteka gtkunique.

%prep
%setup -q

%build
cp /usr/share/automake/mkinstalldirs .
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
