# RPMs for Hugo

## RPM Installation

```
yum install 
```

## RPM Build

#### Install rpmbuild requirements

```
yum install -y spectool git mock
```

### Setup build environment

```
cd ~
git clone https://github.com/daftaupe/hugo-rpms.git
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
ln -s ~/hugo-rpms/SPECS/hugo.spec ~/rpmbuild/SPECS/hugo.spec
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
cd ~/rpmbuild/SOURCES/
spectool -g ../SPECS/hugo.spec
cd ~/rpmbuild/SPECS/
```
### Build the SRPM
```
mock --resultdir ~/rpmbuild/SRPMS --buildsrpm --spec ~/rpmbuild/SPECS/hugo.spec --sources ~/rpmbuild/SOURCES/v0.18.1.tar.gz
# Get the SRPM in ~/rpmbuild/SRPMS
# On Fedora 25 you get hugo-0.18.1-0.fc25.src.rpm
# On Centos  7 you get hugo-0.18.1-0.el7.centos.src.rpm
```

### Build the RPM from the SRPM
Either you get directly the SRPM from the release section on Github or you build it as indicated before (in that case be careful about the name of the SRPM you will get).
```
#RPM file will be found in ~/rpmbuild/RPMS
# Centos7-64bits
mock --cleanup-after --resultdir ~/rpmbuild/RPMS -r epel-7-x86_64 ~/rpmbuild/SRPMS/hugo-0.18.1-0.fc25.src.rpm
# Fedora-25-64bits
mock --cleanup-after --resultdir ~/rpmbuild/SRPMS -r fedora-25-x86_64 ~/rpmbuild/SRPMS/hugo-0.18.1-0.fc25.src.rpm
# Fedora-25-32bits
mock --cleanup-after --resultdir ~/rpmbuild/SRPMS -r fedora-25-i386 ~/rpmbuild/SRPMS/hugo-0.18.1-0.fc25.src.rpm
```

### Usage

See the official [documentation](https://gohugo.io/overview/usage/)
