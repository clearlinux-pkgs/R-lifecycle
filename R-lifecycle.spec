#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lifecycle
Version  : 0.2.0
Release  : 8
URL      : https://cran.r-project.org/src/contrib/lifecycle_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lifecycle_0.2.0.tar.gz
Summary  : Manage the Life Cycle of your Package Functions
Group    : Development/Tools
License  : GPL-3.0
Requires: R-glue
Requires: R-rlang
BuildRequires : R-glue
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
shared conventions, documentation badges, and non-invasive
    deprecation warnings. The 'lifecycle' package defines four
    development stages (experimental, maturing, stable, and
    questioning) and three deprecation stages (soft-deprecated,
    deprecated, and defunct). It makes it easy to insert badges
    corresponding to these stages in your documentation. Usage of
    deprecated functions are signalled with increasing levels of
    non-invasive verbosity.

%prep
%setup -q -c -n lifecycle
cd %{_builddir}/lifecycle

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589826032

%install
export SOURCE_DATE_EPOCH=1589826032
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lifecycle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lifecycle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lifecycle
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc lifecycle || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lifecycle/DESCRIPTION
/usr/lib64/R/library/lifecycle/INDEX
/usr/lib64/R/library/lifecycle/Meta/Rd.rds
/usr/lib64/R/library/lifecycle/Meta/features.rds
/usr/lib64/R/library/lifecycle/Meta/hsearch.rds
/usr/lib64/R/library/lifecycle/Meta/links.rds
/usr/lib64/R/library/lifecycle/Meta/nsInfo.rds
/usr/lib64/R/library/lifecycle/Meta/package.rds
/usr/lib64/R/library/lifecycle/Meta/vignette.rds
/usr/lib64/R/library/lifecycle/NAMESPACE
/usr/lib64/R/library/lifecycle/NEWS.md
/usr/lib64/R/library/lifecycle/R/lifecycle
/usr/lib64/R/library/lifecycle/R/lifecycle.rdb
/usr/lib64/R/library/lifecycle/R/lifecycle.rdx
/usr/lib64/R/library/lifecycle/doc/index.html
/usr/lib64/R/library/lifecycle/doc/lifecycle.R
/usr/lib64/R/library/lifecycle/doc/lifecycle.Rmd
/usr/lib64/R/library/lifecycle/doc/lifecycle.html
/usr/lib64/R/library/lifecycle/help/AnIndex
/usr/lib64/R/library/lifecycle/help/aliases.rds
/usr/lib64/R/library/lifecycle/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/lifecycle/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/lifecycle/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/lifecycle/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/lifecycle/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/lifecycle/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/lifecycle/help/figures/lifecycle-retired.svg
/usr/lib64/R/library/lifecycle/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/lifecycle/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/lifecycle/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/lifecycle/help/lifecycle.rdb
/usr/lib64/R/library/lifecycle/help/lifecycle.rdx
/usr/lib64/R/library/lifecycle/help/macros/lifecycle.Rd
/usr/lib64/R/library/lifecycle/help/paths.rds
/usr/lib64/R/library/lifecycle/html/00Index.html
/usr/lib64/R/library/lifecycle/html/R.css
/usr/lib64/R/library/lifecycle/tests/testthat.R
/usr/lib64/R/library/lifecycle/tests/testthat/error/test-signal-deprecated.txt
/usr/lib64/R/library/lifecycle/tests/testthat/error/test-spec.txt
/usr/lib64/R/library/lifecycle/tests/testthat/helper-lifecycle.R
/usr/lib64/R/library/lifecycle/tests/testthat/output/test-signal-message-args.txt
/usr/lib64/R/library/lifecycle/tests/testthat/output/test-signal-message-non-syntactic.txt
/usr/lib64/R/library/lifecycle/tests/testthat/output/test-signal-message.txt
/usr/lib64/R/library/lifecycle/tests/testthat/output/test-warning-backtrace.txt
/usr/lib64/R/library/lifecycle/tests/testthat/test-arg.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-expect.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-lifecycle.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-signal-deprecated.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-signal.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-spec.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-verbosity.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-warning.R
