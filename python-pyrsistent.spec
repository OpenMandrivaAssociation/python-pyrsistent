# Created by pyp2rpm-3.3.2
%global pypi_name pyrsistent

Name:		python-%{pypi_name}
Version:	0.20.0
Release:	1
Summary:	Persistent/Functional/Immutable data structures
Group:		Development/Python
License:	MIT
URL:		https://github.com/tobgu/pyrsistent/
Source0:	https://files.pythonhosted.org/packages/source/p/pyrsistent/pyrsistent-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(six)
BuildRequires:  python%{pyver}dist(pip)
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:	python%{pyver}dist(six)
BuildArch:	noarch

%description
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
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%doc README.rst
#{python3_sitearch}/pvectorc.*.so
%{python3_sitearch}/_pyrsistent_version.py
%dir %{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}/*
%{python3_sitearch}/%{pypi_name}-*.dist-info
%{python3_sitearch}/__pycache__/_pyrsistent_version.cpython-*.pyc
