Summary:	Simple IRC client
Summary(pl):	Prosty klient IRC
Name:		lostirc
Version:	0.4.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/lostirc/%{name}-%{version}.tar.gz
# Source0-md5:	5f3c0ec0c4fe3ed41e6a349f9c52a0bf
Patch0:		%{name}-desktop.patch
URL:		http://lostirc.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-autopoint
BuildRequires:	gtkmm-devel >= 2.4
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LostIRC is a simple, keyboard controlled IRC client.

%description -l pl
LostIRC jest prostym klientem IRC kotrolowanym przy pomocy klawiatury.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autopoint}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-kde
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_mandir}/man1/lostirc.1.*
%{_pixmapsdir}/*