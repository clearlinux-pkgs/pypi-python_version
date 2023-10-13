#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-python_version
Version  : 0.0.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/fe/74/8ed1d7f895b33a89565be4b1c8651d503fcb2cdda951fef4ec6f6906432c/python_version-0.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/fe/74/8ed1d7f895b33a89565be4b1c8651d503fcb2cdda951fef4ec6f6906432c/python_version-0.0.2.tar.gz
Summary  : Provides a simple utility for checking the python version.
Group    : Development/Tools
License  : MIT
Requires: pypi-python_version-python = %{version}-%{release}
Requires: pypi-python_version-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
This package provides a basic python version checking utility.  
        It will check for a range of python versions and either report
        an error or exit depending on the parameters provided.
        
        ## Example
        
        ```
        $ python

%package python
Summary: python components for the pypi-python_version package.
Group: Default
Requires: pypi-python_version-python3 = %{version}-%{release}

%description python
python components for the pypi-python_version package.


%package python3
Summary: python3 components for the pypi-python_version package.
Group: Default
Requires: python3-core
Provides: pypi(python_version)

%description python3
python3 components for the pypi-python_version package.


%prep
%setup -q -n python_version-0.0.2
cd %{_builddir}/python_version-0.0.2
pushd ..
cp -a python_version-0.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659485484
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
