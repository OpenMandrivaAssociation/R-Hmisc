%define modulename Hmisc
%define realver 3.7-0
%define r_library %{_libdir}/R/library
%define _requires_exceptions libR.so

Summary:        Harrell Miscellaneous for R
Name:           R-cran-%{modulename}
Version:        %(echo %{realver} | tr '-' '.')
Release:        %mkrel 1
License:        GPLv2+
Group:          Sciences/Mathematics
Url:            http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:        http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:  R-base
BuildRequires:  gcc-gfortran
Requires:       R-base
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
The Hmisc library contains many functions useful for data analysis,
high-level graphics, utility operations, functions for computing
sample size and power, importing datasets, imputing missing values,
advanced table making, variable clustering, character string
manipulation, conversion of S objects to LaTeX code, and recoding
variables.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
