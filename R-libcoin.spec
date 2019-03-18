#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-libcoin
Version  : 1.0.4
Release  : 20
URL      : https://cran.r-project.org/src/contrib/libcoin_1.0-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/libcoin_1.0-4.tar.gz
Summary  : Linear Test Statistics for Permutation Inference
Group    : Development/Tools
License  : GPL-2.0
Requires: R-libcoin-lib = %{version}-%{release}
Requires: R-matrixStats
Requires: R-modeltools
Requires: R-multcomp
BuildRequires : R-TH.data
BuildRequires : R-coin
BuildRequires : R-matrixStats
BuildRequires : R-modeltools
BuildRequires : R-multcomp
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-libcoin package.
Group: Libraries

%description lib
lib components for the R-libcoin package.


%prep
%setup -q -c -n libcoin

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552809566

%install
export SOURCE_DATE_EPOCH=1552809566
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library libcoin
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library libcoin
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library libcoin
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  libcoin || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/libcoin/DESCRIPTION
/usr/lib64/R/library/libcoin/INDEX
/usr/lib64/R/library/libcoin/Meta/Rd.rds
/usr/lib64/R/library/libcoin/Meta/features.rds
/usr/lib64/R/library/libcoin/Meta/hsearch.rds
/usr/lib64/R/library/libcoin/Meta/links.rds
/usr/lib64/R/library/libcoin/Meta/nsInfo.rds
/usr/lib64/R/library/libcoin/Meta/package.rds
/usr/lib64/R/library/libcoin/Meta/vignette.rds
/usr/lib64/R/library/libcoin/NAMESPACE
/usr/lib64/R/library/libcoin/NEWS.Rd
/usr/lib64/R/library/libcoin/R/libcoin
/usr/lib64/R/library/libcoin/R/libcoin.rdb
/usr/lib64/R/library/libcoin/R/libcoin.rdx
/usr/lib64/R/library/libcoin/doc/index.html
/usr/lib64/R/library/libcoin/doc/libcoin.R
/usr/lib64/R/library/libcoin/doc/libcoin.Rnw
/usr/lib64/R/library/libcoin/doc/libcoin.pdf
/usr/lib64/R/library/libcoin/help/AnIndex
/usr/lib64/R/library/libcoin/help/aliases.rds
/usr/lib64/R/library/libcoin/help/libcoin.rdb
/usr/lib64/R/library/libcoin/help/libcoin.rdx
/usr/lib64/R/library/libcoin/help/paths.rds
/usr/lib64/R/library/libcoin/html/00Index.html
/usr/lib64/R/library/libcoin/html/R.css
/usr/lib64/R/library/libcoin/include/libcoin.h
/usr/lib64/R/library/libcoin/include/libcoinAPI.h
/usr/lib64/R/library/libcoin/include/libcoin_internal.h
/usr/lib64/R/library/libcoin/libcoin.bib
/usr/lib64/R/library/libcoin/tests/bugfixes.R
/usr/lib64/R/library/libcoin/tests/bugfixes.Rout.save
/usr/lib64/R/library/libcoin/tests/libcoin.R
/usr/lib64/R/library/libcoin/tests/regtest_ctabs.R
/usr/lib64/R/library/libcoin/tests/regtest_ctabs.Rout.save
/usr/lib64/R/library/libcoin/tests/regtest_libcoin.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/libcoin/libs/libcoin.so
/usr/lib64/R/library/libcoin/libs/libcoin.so.avx2
/usr/lib64/R/library/libcoin/libs/libcoin.so.avx512
