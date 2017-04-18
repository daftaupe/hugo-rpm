%define debug_package %{nil}
Name:		hugo
Version:	0.20.1
Release:	0%{?dist}
Summary:	A Fast and Flexible Static Site Generator

Group:		Applications/System
License:	Apache 2.0
URL:		https://github.com/spf13/hugo
Source0:	https://github.com/spf13/hugo/archive/v%{version}.tar.gz

BuildRequires:  git golang

%description
Hugo is a static HTML and CSS website generator written in Go. It is optimized for speed, easy use and configurability. Hugo takes a directory with content and templates and renders them into a full HTML website.

%prep
%setup -q 

%build
export GOPATH="$(pwd)"
export PATH=$PATH:"$(pwd)"/bin
mkdir -p src/github.com/spf13/
ln -s "$(pwd)" src/github.com/spf13/hugo
cd src/github.com/spf13/hugo
make govendor
go get github.com/spf13/hugo

%install
mkdir -p %{buildroot}%{_bindir}
#mkdir -p %{buildroot}%{_unitdir}
#mkdir -p %{buildroot}%{_userunitdir}

cp bin/hugo %{buildroot}%{_bindir}
#cp etc/linux-systemd/system/syncthing\@.service  %{buildroot}%{_unitdir}
#cp etc/linux-systemd/system/syncthing-resume.service  %{buildroot}%{_unitdir}
#cp etc/linux-systemd/user/syncthing.service %{buildroot}%{_userunitdir}


%files
%{_bindir}/hugo
#%{_unitdir}/syncthing@.service
#%{_unitdir}/syncthing-resume.service
#%{_userunitdir}/syncthing.service

%changelog
* Tue Apr 18 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.20.1-0
- New release 0.20.1
* Tue Apr 18 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.20-0
- New release 0.20
* Mon Feb 27 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.19-0
- New release 0.19
* Sat Feb 11 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.18.1-0
- Initial version of the rpm
