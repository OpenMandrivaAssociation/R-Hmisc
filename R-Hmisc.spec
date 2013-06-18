%bcond_with bootstrap
%global packname  Hmisc
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.10.1
Release:          2
Summary:          Harrell Miscellaneous
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Hmisc_3.10-1.tar.gz
Requires:         R-methods R-survival R-lattice R-cluster
%if %{without bootstrap}
Requires:         R-grid R-nnet R-foreign R-chron R-acepack R-subselect R-tree
Requires:         R-TeachingDemos R-rms R-mice
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-survival R-lattice R-cluster
%if %{without bootstrap}
BuildRequires:    R-grid R-nnet R-foreign R-chron R-acepack R-subselect R-tree
BuildRequires:    R-TeachingDemos R-rms R-mice
%endif

%description
The Hmisc library contains many functions useful for data analysis,
high-level graphics, utility operations, functions for computing sample
size and power, importing datasets, imputing missing values, advanced
table making, variable clustering, character string manipulation,
conversion of S objects to LaTeX code, and recoding variables.  Please
submit bug reports to 'http://biostat.mc.vanderbilt.edu/trac/Hmisc'.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/todo
%doc %{rlibdir}/%{packname}/CHANGELOG
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/WISHLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
