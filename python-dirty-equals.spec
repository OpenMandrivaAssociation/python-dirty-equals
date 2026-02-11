%define module dirty-equals
%define oname dirty_equals

%bcond tests 1

Name:		python-dirty-equals
Version:	0.11
Release:	1
Summary:	Doing dirty (but extremely useful) things with equals
License:	MIT
Group:		Development/Python
URL:		https://github.com/samuelcolvin/dirty-equals
Source0:	https://files.pythonhosted.org/packages/source/d/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pydantic)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-examples)
BuildRequires:	python%{pyver}dist(pytest-mock)
BuildRequires:	python%{pyver}dist(pytz)
%endif
Requires:	python%{pyver}dist(pytz) >= 2021.3

%description
Doing dirty (but extremely useful) things with equals.

dirty-equals is a python library that (mis)uses the __eq__ method to make
python code (generally unit tests) more declarative and therefore easier
to read and write.

dirty-equals can be used in whatever context you like, but it comes into
its own when writing unit tests for applications where you're commonly
checking the response to API calls and the contents of a database.

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
# Skip failing tests in py3.14 - https://github.com/samuelcolvin/dirty-equals/issues/112
pytest tests/ -k "not test_is_ip_true"
%endif

%files
%doc README.md
%license LICENSE
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info/
