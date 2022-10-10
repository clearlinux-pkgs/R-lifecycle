#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lifecycle
Version  : 1.0.3
Release  : 28
URL      : https://cran.r-project.org/src/contrib/lifecycle_1.0.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lifecycle_1.0.3.tar.gz
Summary  : Manage the Life Cycle of your Package Functions
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-glue
Requires: R-rlang
BuildRequires : R-cli
BuildRequires : R-glue
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
conventions, documentation badges, and user-friendly deprecation
    warnings.

%prep
%setup -q -n lifecycle
cd %{_builddir}/lifecycle

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665425163

%install
export SOURCE_DATE_EPOCH=1665425163
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lifecycle/DESCRIPTION
/usr/lib64/R/library/lifecycle/INDEX
/usr/lib64/R/library/lifecycle/LICENSE
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
/usr/lib64/R/library/lifecycle/doc/communicate.R
/usr/lib64/R/library/lifecycle/doc/communicate.Rmd
/usr/lib64/R/library/lifecycle/doc/communicate.html
/usr/lib64/R/library/lifecycle/doc/index.html
/usr/lib64/R/library/lifecycle/doc/manage.R
/usr/lib64/R/library/lifecycle/doc/manage.Rmd
/usr/lib64/R/library/lifecycle/doc/manage.html
/usr/lib64/R/library/lifecycle/doc/stages.R
/usr/lib64/R/library/lifecycle/doc/stages.Rmd
/usr/lib64/R/library/lifecycle/doc/stages.html
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
/usr/lib64/R/library/lifecycle/tests/testthat/_snaps/badge.md
/usr/lib64/R/library/lifecycle/tests/testthat/_snaps/deprecate.md
/usr/lib64/R/library/lifecycle/tests/testthat/_snaps/signal.md
/usr/lib64/R/library/lifecycle/tests/testthat/_snaps/spec.md
/usr/lib64/R/library/lifecycle/tests/testthat/_snaps/warning.md
/usr/lib64/R/library/lifecycle/tests/testthat/helper-lifecycle.R
/usr/lib64/R/library/lifecycle/tests/testthat/helper-zeallot.R
/usr/lib64/R/library/lifecycle/tests/testthat/output/test-signal-message-args.txt
/usr/lib64/R/library/lifecycle/tests/testthat/output/test-signal-message-non-syntactic.txt
/usr/lib64/R/library/lifecycle/tests/testthat/output/test-signal-message.txt
/usr/lib64/R/library/lifecycle/tests/testthat/output/test-warning-backtrace.txt
/usr/lib64/R/library/lifecycle/tests/testthat/test-arg.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-badge.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-deprecate.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-expect.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-lifecycle.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-signal.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-spec.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-verbosity.R
/usr/lib64/R/library/lifecycle/tests/testthat/test-warning.R
