%global pname k8sclient
%global sname python-k8sclient

%if 0%{?fedora} >= 24
%global with_python3 1
%global _docdir_fmt %{name}
%endif

Name:           python-k8sclient
Version:        XXX
Release:        XXX
Summary:        Python API for Kubernetes

License:        ASL 2.0
URL:            https://github.com/openstack/python-k8sclient
Source0:        https://pypi.python.org/packages/source/p/%{sname}/%{sname}-%{version}.tar.gz
BuildArch:      noarch

%description
This is Kubernetes API python client code. This code is generated by
swagger-codegen. Kubernetes provide swagger-spec to generate client code
for different versions.


%package -n     python2-k8sclient
Summary:        Python API for Kubernetes

%{?python_provide:%python_provide python2-%{pname}}

BuildRequires:  python-pbr >= 1.8
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-six

Requires:       python-pbr >= 1.8
Requires:       python-six >= 1.9.0
Requires:       python-urllib3 >= 1.8.3
Requires:       python-dateutil

# test requirements

BuildRequires:       python-hacking
BuildRequires:       python-coverage
BuildRequires:       python-subunit
BuildRequires:       python-oslotest
BuildRequires:       python-testrepository
BuildRequires:       python-testscenarios
BuildRequires:       python-testtools

%description -n python2-k8sclient
This is Kubernetes API python client code. This code is generated by
swagger-codegen. Kubernetes provide swagger-spec to generate client code
for different versions.

%if 0%{?with_python3}
%package -n     python3-k8sclient
Summary:        Python API for Kubernetes

%{?python_provide:%python_provide python3-%{pname}}

BuildRequires:  python3-pbr >= 1.8
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

Requires:       python3-pbr >= 1.8
Requires:       python3-six >= 1.9.0
Requires:       python3-urllib3 >= 1.8.3
Requires:       python3-dateutil

# test requirements

BuildRequires:       python3-hacking
BuildRequires:       python3-coverage
BuildRequires:       python3-subunit
BuildRequires:       python3-oslotest
BuildRequires:       python3-testrepository
BuildRequires:       python3-testscenarios
BuildRequires:       python3-testtools

%description -n python3-k8sclient
This is Kubernetes API python client code. This code is generated by
swagger-codegen. Kubernetes provide swagger-spec to generate client code
for different versions.
%endif

%package -n python-%{pname}-doc
Summary:        Python k8sclient documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

%description -n python-%{pname}-doc
Documentation for python-k8sclient

%prep
%autosetup -n %{name}-%{upstream_version}

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3}
%py3_install
%endif

%py2_install

%check
# Skipping the tests due to this pbr bug
# https://bugs.launchpad.net/pbr/+bug/1505007
python2 setup.py test ||

%if 0%{?with_python3}
python3 setup.py test ||
rm -rf .testrepository
%endif

%files -n python2-k8sclient
%doc README.rst
%license LICENSE
%{python2_sitelib}/k8sclient
%{python2_sitelib}/python_k8sclient-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-k8sclient
%doc README.rst
%license LICENSE
%{python3_sitelib}/k8sclient
%{python3_sitelib}/python_k8sclient-%{version}-py?.?.egg-info
%endif

%files -n python-%{pname}-doc
%doc html doc/source/readme.rst

%changelog
