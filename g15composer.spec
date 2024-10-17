Name:                   g15composer
Version:                3.2
Release:                6
Summary:                Scriptable command interface to libg15render drawing functions
License:                GPLv2+
Group:                  System/Configuration/Hardware
URL:                    https://g15tools.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15tools/g15composer-%{version}.tar.bz2
BuildRequires:          bison
BuildRequires:          flex
BuildRequires:          g15-devel
BuildRequires:          g15daemon_client-devel
BuildRequires:          g15render-devel

%description
G15composer is a scriptable command interface to the libg15render drawing
functions that outputs to a g15daemon screen. G15composer exposes all
graphics primitives and text rendering functions of libg15render so that
they may be used in a variety of situations, including from the command
line or in virtually any scripting language.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README examples/ 
%defattr(-,root,root,0755)
%{_bindir}/g15composer
%{_mandir}/man1/g15composer.1*


%changelog
* Thu Sep 03 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.2-4mdv2010.0
+ Revision: 428981
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.2-3mdv2009.0
+ Revision: 245587
- rebuild

* Fri Feb 08 2008 David Walluck <walluck@mandriva.org> 3.2-1mdv2008.1
+ Revision: 163919
- fix URL
- import g15composer


