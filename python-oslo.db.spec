#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (incomplete dependencies)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Oslo Database library
Summary(pl.UTF-8):	Biblioteka Oslo Database
Name:		python-oslo.db
# keep 6.x here for python2 support
Version:	6.0.0
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/oslo.db/
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.db/oslo.db-%{version}.tar.gz
# Source0-md5:	0c3ceffd6d4dfe2532cce0de44806dd3
URL:		https://pypi.org/project/oslo.db/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 3.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-alembic >= 0.9.6
BuildRequires:	python-debtcollector >= 1.2.0
BuildRequires:	python-eventlet >= 0.18.4
BuildRequires:	python-fixtures >= 3.0.0
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-os-testr >= 1.0.0
BuildRequires:	python-oslo.config >= 5.2.0
BuildRequires:	python-oslo.context >= 2.19.2
BuildRequires:	python-oslo.i18n >= 3.15.3
BuildRequires:	python-oslo.utils >= 3.33.0
BuildRequires:	python-oslotest >= 3.2.0
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-sqlalchemy >= 1.2.0
BuildRequires:	python-sqlalchemy-migrate >= 0.11.0
BuildRequires:	python-stestr >= 2.0.0
BuildRequires:	python-stevedore >= 1.20.0
BuildRequires:	python-subunit >= 1.0.0
BuildRequires:	python-testresources >= 2.0.0
BuildRequires:	python-testscenarios >= 0.4
BuildRequires:	python-testtools >= 2.2.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-pbr >= 3.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
%if %{with tests}
BuildRequires:	python3-alembic >= 0.9.6
BuildRequires:	python3-debtcollector >= 1.2.0
BuildRequires:	python3-eventlet >= 0.18.4
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-os-testr >= 1.0.0
BuildRequires:	python3-oslo.config >= 5.2.0
BuildRequires:	python3-oslo.context >= 2.19.2
BuildRequires:	python3-oslo.i18n >= 3.15.3
BuildRequires:	python3-oslo.utils >= 3.33.0
BuildRequires:	python3-oslotest >= 3.2.0
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-sqlalchemy >= 1.2.0
BuildRequires:	python3-sqlalchemy-migrate >= 0.11.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-stevedore >= 1.20.0
BuildRequires:	python3-subunit >= 1.0.0
BuildRequires:	python3-testresources >= 2.0.0
BuildRequires:	python3-testscenarios >= 0.4
BuildRequires:	python3-testtools >= 2.2.0
%endif
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-alembic >= 0.9.6
BuildRequires:	python-openstackdocstheme >= 1.20.0
BuildRequires:	python-oslo.config >= 5.2.0
BuildRequires:	python-oslo.utils >= 3.33.0
BuildRequires:	python-reno >= 2.5.0
#BuildRequires:	python-oslotest >= 3.2.0
BuildRequires:	python-sphinxcontrib-apidoc >= 0.2.0
BuildRequires:	python-sqlalchemy-migrate >= 0.11.0
BuildRequires:	python-stevedore >= 1.20.0
BuildRequires:	sphinx-pdg-2 >= 1.8.0
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The oslo db (database) handling library, provides database
connectivity to different database backends and various other helper
utils.

%description -l pl.UTF-8
Biblioteka oslo db to biblioteka do obsługi baz danych, zapewniająca
łączność z różnymi backendami baz danych oraz różne inne narzędzia
pomocnicze.

%package -n python3-oslo.db
Summary:	Oslo Database library
Summary(pl.UTF-8):	Biblioteka Oslo Database
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-oslo.db
The oslo db (database) handling library, provides database
connectivity to different database backends and various other helper
utils.

%description -n python3-oslo.db -l pl.UTF-8
Biblioteka oslo db to biblioteka do obsługi baz danych, zapewniająca
łączność z różnymi backendami baz danych oraz różne inne narzędzia
pomocnicze.

%package apidocs
Summary:	API documentation for Python oslo.db module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona oslo.db
Group:		Documentation

%description apidocs
API documentation for Python oslo.db module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona oslo.db.

%prep
%setup -q -n oslo.db-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
sphinx-build-2 doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/oslo_db/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/oslo_db/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/oslo_db
%{py_sitescriptdir}/oslo.db-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-oslo.db
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/oslo_db
%{py3_sitescriptdir}/oslo.db-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,install,reference,user,*.html,*.js}
%endif
