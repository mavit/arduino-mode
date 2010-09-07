%global pkg arduino-mode
%global pkgname Arduino Mode
%global gitcommit 16e1d57

Name:		emacs-common-%{pkg}
Version:	git1.%{gitcommit}
Release:	1%{?dist}
Summary:	Emacs editing mode for Arduino code

Group:		Development/Tools
License:	GPLv3+
URL:		http://github.com/mavit/%{pkg}/
Source0:	http://download.github.com/mavit-%{pkg}-%{gitcommit}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	emacs
BuildRequires:	xemacs
Requires:	arduino

%description
%{pkgname} is an add-on package for GNU Emacs and XEmacs, providing an
editing mode for the Arduino electronics prototyping platform.

This package contains the files common to both the GNU Emacs and XEmacs
%{pkgname} packages.

%package -n emacs-%{pkg}
Summary:	Compiled elisp files to run %{pkgname} under GNU Emacs
Group:		Development/Tools
Requires:	emacs(bin) >= %{_emacs_version}
Requires:	emacs-common-%{pkg} = %{version}-%{release}

%description -n emacs-%{pkg}
This package contains the byte compiled elisp packages to run 
%{pkgname} with GNU Emacs.


%package -n emacs-%{pkg}-el
Summary:	Elisp source files for %{pkgname} under GNU Emacs
Group:		Development/Tools
Requires:	emacs-%{pkg} = %{version}-%{release}

%description -n emacs-%{pkg}-el
This package contains the elisp source files for %{pkgname} under GNU
Emacs. You do not need to install this package to run
%{pkgname}. Install the emacs-%{pkg} package to use %{pkgname} with 
GNU Emacs.


%package -n xemacs-%{pkg}
Summary:	Compiled elisp files to run %{pkgname} under XEmacs
Group:		Development/Tools
Requires:	xemacs(bin) >= %{_xemacs_version}
Requires:	emacs-common-%{pkg} = %{version}-%{release}

%description -n xemacs-%{pkg}
This package contains the byte compiled elisp packages to use %{pkgname}
with XEmacs.


%package -n xemacs-%{pkg}-el
Summary:	Elisp source files for %{pkgname} under XEmacs
Group:		Development/Tools
Requires:	xemacs-%{pkg} = %{version}-%{release}

%description -n xemacs-%{pkg}-el
This package contains the elisp source files for %{pkgname} under
XEmacs. You do not need to install this package to run
%{pkgname}. Install the xemacs-%{pkg} package to use %{pkgname} with
XEmacs.


%prep
%setup -q -n mavit-%{pkg}-%{gitcommit}

%build
%{_emacs_bytecompile} %{pkg}.el
%{_xemacs_bytecompile} %{pkg}.el

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_emacs_sitelispdir}/%{pkg} \
	 $RPM_BUILD_ROOT/%{_xemacs_sitelispdir}/%{pkg} \
	 $RPM_BUILD_ROOT/%{_emacs_sitestartdir} \
	 $RPM_BUILD_ROOT/%{_xemacs_sitestartdir}
cp -a %{pkg}.el %{pkg}.elc $RPM_BUILD_ROOT/%{_emacs_sitelispdir}/%{pkg}/
cp -a %{pkg}.el %{pkg}.elc $RPM_BUILD_ROOT/%{_xemacs_sitelispdir}/%{pkg}/
cp -a %{pkg}-init.el $RPM_BUILD_ROOT/%{_emacs_sitestartdir}/
cp -a %{pkg}-init.el $RPM_BUILD_ROOT/%{_xemacs_sitestartdir}/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc


%files -n emacs-%{pkg}
%defattr(-,root,root,-)
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitestartdir}/*.el
%dir %{_emacs_sitelispdir}/%{pkg}


%files -n emacs-%{pkg}-el
%defattr(-,root,root,-)
%{_emacs_sitelispdir}/%{pkg}/*.el


%files -n xemacs-%{pkg}
%defattr(-,root,root,-)
%{_xemacs_sitelispdir}/%{pkg}/*.elc
%{_xemacs_sitestartdir}/*.el
%dir %{_xemacs_sitelispdir}/%{pkg}


%files -n xemacs-%{pkg}-el
%defattr(-,root,root,-)
%{_xemacs_sitelispdir}/%{pkg}/*.el


%changelog
* Tue Sep  7 2010  <rpm@mavit.org.uk> - git1.16e1d57-1
- Initial version.

