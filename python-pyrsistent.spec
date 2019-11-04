# Created by pyp2rpm-3.3.2
%global pypi_name pyrsistent

Name:           python-%{pypi_name}
Version:	0.15.5
Release:	1
Summary:        Persistent/Functional/Immutable data structures
Group:          Development/Python
License:        MIT
URL:            https://github.com/tobgu/pyrsistent/
Source0:	https://files.pythonhosted.org/packages/30/86/53a88c0a57698fa228db29a4000c28f4124823010388cb7042fe6e2be8dd/pyrsistent-0.15.5.tar.gz

BuildRequires:  python2-devel
BuildRequires:	python2dist(enum34)
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2dist(six)

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(six)

%description
Pyrsistent is a number of persistent collections (by some referred to as
functional data structures). Persistent in the sense that they are immutable.

All methods on a data structure that would normally mutate it instead return
a new copy of the structure containing the requested updates. The original
structure is left untouched.

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:       python2dist(six)

%description -n python2-%{pypi_name}
Pyrsistent is a number of persistent collections (by some referred to as
functional data structures). Persistent in the sense that they are immutable.

All methods on a data structure that would normally mutate it instead return
a new copy of the structure containing the requested updates. The original
structure is left untouched.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%files -n python2-%{pypi_name}
%doc README.rst
%{python2_sitearch}/pvectorc.so
%{python2_sitearch}/_pyrsistent_version.py*
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}
%doc README.rst
%{python3_sitearch}/pvectorc.*.so
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/_pyrsistent_version.py
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
