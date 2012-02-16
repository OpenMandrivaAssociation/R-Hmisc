%global packname  Hmisc
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.9_1
Release:          1
Summary:          Harrell Miscellaneous
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              None
Source0:          http://cran.r-project.org/src/contrib/Archive/Hmisc/Hmisc_3.9-1.tar.gz
Requires:         R-methods R-survival 
Requires:         R-lattice R-cluster R-survival 
Requires:         R-lattice R-grid R-nnet R-foreign R-chron R-acepack R-TeachingDemos R-rms R-cluster R-mice R-subselect R-tree 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-survival
BuildRequires:    R-lattice R-cluster R-survival 
BuildRequires:    R-lattice R-grid R-nnet R-foreign R-chron R-acepack R-TeachingDemos R-rms R-cluster R-mice R-subselect R-tree 
%rename R-cran-Hmisc

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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
