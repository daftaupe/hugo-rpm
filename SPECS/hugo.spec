%define debug_package %{nil}
Name:           hugo
Version:        0.40.2
Release:        1%{?dist}
Summary:        A Fast and Flexible Static Site Generator

Group:          Applications/System
License:        Apache 2.0
URL:            https://github.com/gohugoio/hugo
Source0:        https://github.com/gohugoio/hugo/archive/v%{version}.tar.gz

BuildRequires:  git golang

%description
Hugo is a static HTML and CSS website generator written in Go. It is optimized for speed, easy use and configurability. Hugo takes a directory with content and templates and renders them into a full HTML website.

%prep
mkdir -p %{_builddir}/src/github.com/gohugoio/
cd %{_builddir}/src/github.com/gohugoio/
tar -xvzf %{_sourcedir}/v%{version}.tar.gz 
mv hugo-%{version} hugo
cd hugo

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
go get -u github.com/golang/dep/cmd/dep
cd %{_builddir}/src/github.com/gohugoio/hugo
dep ensure
go get github.com/magefile/mage
mage hugo
mage install

%install
mkdir -p %{buildroot}%{_bindir}

cp %{_builddir}/bin/hugo %{buildroot}%{_bindir}


%files
%{_bindir}/hugo

%changelog
* Mon Apr 30 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.40.2-1
- New release 0.40.2

* Thu Apr 26 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.40.1-1
- New release 0.40.1

* Mon Apr 23 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.40-1
- New release 0.40

* Tue Apr 17 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.39-0
- New release 0.39

* Mon Apr 09 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.38.2-0
- New release 0.38.2

* Fri Apr 06 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.38.1-0
- New release 0.38.1

* Wed Apr 04 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.38-0
- New release 0.38

* Thu Mar 15 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.37.1-0
- New release 0.37.1

* Tue Feb 27 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.37-0
- New release 0.37

* Fri Feb 23 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.36.1-0
- New release 0.36.1

* Wed Feb 07 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.36-0
- New release 0.36

* Sat Feb 03 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.35-0
- New release 0.35

* Sun Jan 28 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.34-0
- New release 0.34

* Sun Jan 21 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.33-0
- New release 0.33

* Sat Jan 13 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.32.4-0
- New release 0.32.4

* Sat Jan 13 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.32.3-0
- New release 0.32.3

* Sat Jan 06 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.32.2-0
- New release 0.32.2

* Tue Jan 02 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.32.1-0
- New release 0.32.1

* Tue Jan 02 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.32-0
- New release 0.32

* Mon Nov 27 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.31.1-0
- New release 0.31.1

* Mon Nov 20 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.31-0
- New release 0.31

* Thu Oct 19 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.30.2-0
- New release 0.30.2
- Adapt the build process to dep

* Thu Oct 19 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.30.1-0
- New release 0.30.1
- Adapt to mage build process

* Mon Oct 16 2017 daftaupe <daftaupe@protonmail.com> 0.30-0
- New release 0.30

* Thu Sep 28 2017 daftaupe <daftaupe@protonmail.com> 0.29-0
- New release 0.29
- Clean the changelog

* Thu Sep 28 2017 daftaupe <daftaupe@protonmail.com> 0.28-0
- New release 0.28

* Tue Sep 12 2017 daftaupe <daftaupe@protonmail.com> 0.27-0
- New release 0.27

* Fri Aug 25 2017 daftaupe <daftaupe@protonmail.com> 0.26-0
- New release 0.26

* Tue Jul 25 2017 daftaupe <daftaupe@protonmail.com> 0.25.1-0
- New release 0.25.1

* Tue Jul 25 2017 daftaupe <daftaupe@protonmail.com> 0.25-0
- New release 0.25

* Sat Jun 24 2017 daftaupe <daftaupe@protonmail.com> 0.24.1-0
- New release 0.24.1

* Thu Jun 22 2017 daftaupe <daftaupe@protonmail.com> 0.24-0
- New release 0.24

* Fri Jun 16 2017 daftaupe <daftaupe@protonmail.com> 0.23-0
- New release 0.23
- Update to the new URL of the project on github

* Tue Jun 13 2017 daftaupe <daftaupe@protonmail.com> 0.22.1-0
- New release 0.22.1
- New release 0.22

* Thu May 25 2017 daftaupe <daftaupe@protonmail.com> 0.21-0
- New release 0.21

* Sun May 14 2017 daftaupe <daftaupe@protonmail.com> 0.20.7-0
- New release 0.20.7

* Sun May 14 2017 daftaupe <daftaupe@protonmail.com> 0.20.6-0
- New release 0.20.6

* Sun May 14 2017 daftaupe <daftaupe@protonmail.com> 0.20.5-0
- New release 0.20.5

* Sun May 14 2017 daftaupe <daftaupe@protonmail.com> 0.20.4-0
- New release 0.20.4

* Sun May 14 2017 daftaupe <daftaupe@protonmail.com> 0.20.3-0
- New release 0.20.3

* Tue Apr 18 2017 daftaupe <daftaupe@protonmail.com> 0.20.2-0
- New release 0.20.2

* Tue Apr 18 2017 daftaupe <daftaupe@protonmail.com> 0.20.1-0
- New release 0.20.1

* Tue Apr 18 2017 daftaupe <daftaupe@protonmail.com> 0.20-0
- New release 0.20

* Mon Feb 27 2017 daftaupe <daftaupe@protonmail.com> 0.19-0
- New release 0.19

* Sat Feb 11 2017 daftaupe <daftaupe@protonmail.com> 0.18.1-0
- Initial version of the rpm
