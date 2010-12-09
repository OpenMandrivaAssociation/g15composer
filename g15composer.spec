Name:                   g15composer
Version:                3.2
Release:                %mkrel 5
Summary:                Scriptable command interface to libg15render drawing functions
License:                GPL
Group:                  System/Configuration/Hardware
URL:                    http://g15tools.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15tools/g15composer-%{version}.tar.bz2
BuildRequires:          bison
BuildRequires:          flex
BuildRequires:          g15daemon_client-devel
BuildRequires:          g15render-devel
BuildRoot:              %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README examples/ 
%defattr(-,root,root,0755)
%{_bindir}/g15composer
%{_mandir}/man1/g15composer.1*
