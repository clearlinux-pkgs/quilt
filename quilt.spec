#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA5526B9BB3CD4E6A (jdelvare@suse.de)
#
Name     : quilt
Version  : 0.67
Release  : 15
URL      : https://download.savannah.gnu.org/releases/quilt/quilt-0.67.tar.gz
Source0  : https://download.savannah.gnu.org/releases/quilt/quilt-0.67.tar.gz
Source1  : https://download.savannah.gnu.org/releases/quilt/quilt-0.67.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: quilt-bin = %{version}-%{release}
Requires: quilt-data = %{version}-%{release}
Requires: quilt-license = %{version}-%{release}
Requires: quilt-locales = %{version}-%{release}
Requires: quilt-man = %{version}-%{release}
BuildRequires : ed
BuildRequires : util-linux
Patch1: backport-Avoid-warnings-with-grep-3.8.patch

%description
The scripts allow to manage a series of patches by keeping
track of the changes each patch makes. Patches can be
applied, un-applied, refreshed, etc.

The scripts are heavily based on Andrew Morton's patch scripts
found at http://userweb.kernel.org/~akpm/stuff/patch-scripts.tar.gz.

Authors:
--------
    Andrew Morton <akpm@digeo.com>
    Andreas Gruenbacher <agruen@suse.de>

%package bin
Summary: bin components for the quilt package.
Group: Binaries
Requires: quilt-data = %{version}-%{release}
Requires: quilt-license = %{version}-%{release}

%description bin
bin components for the quilt package.


%package data
Summary: data components for the quilt package.
Group: Data

%description data
data components for the quilt package.


%package doc
Summary: doc components for the quilt package.
Group: Documentation
Requires: quilt-man = %{version}-%{release}

%description doc
doc components for the quilt package.


%package license
Summary: license components for the quilt package.
Group: Default

%description license
license components for the quilt package.


%package locales
Summary: locales components for the quilt package.
Group: Default

%description locales
locales components for the quilt package.


%package man
Summary: man components for the quilt package.
Group: Default

%description man
man components for the quilt package.


%prep
%setup -q -n quilt-0.67
cd %{_builddir}/quilt-0.67
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663010688
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1663010688
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/quilt
cp %{_builddir}/quilt-%{version}/COPYING %{buildroot}/usr/share/package-licenses/quilt/dfac199a7539a404407098a2541b9482279f690d
%make_install
%find_lang quilt

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/guards
/usr/bin/quilt

%files data
%defattr(-,root,root,-)
/usr/share/emacs/site-lisp/quilt.el
/usr/share/quilt/add
/usr/share/quilt/annotate
/usr/share/quilt/applied
/usr/share/quilt/compat/awk
/usr/share/quilt/compat/sendmail
/usr/share/quilt/delete
/usr/share/quilt/diff
/usr/share/quilt/edit
/usr/share/quilt/files
/usr/share/quilt/fold
/usr/share/quilt/fork
/usr/share/quilt/graph
/usr/share/quilt/grep
/usr/share/quilt/header
/usr/share/quilt/import
/usr/share/quilt/mail
/usr/share/quilt/new
/usr/share/quilt/next
/usr/share/quilt/patches
/usr/share/quilt/pop
/usr/share/quilt/previous
/usr/share/quilt/push
/usr/share/quilt/refresh
/usr/share/quilt/remove
/usr/share/quilt/rename
/usr/share/quilt/revert
/usr/share/quilt/scripts/backup-files
/usr/share/quilt/scripts/dependency-graph
/usr/share/quilt/scripts/edmail
/usr/share/quilt/scripts/inspect-wrapper
/usr/share/quilt/scripts/patchfns
/usr/share/quilt/scripts/remove-trailing-ws
/usr/share/quilt/scripts/utilfns
/usr/share/quilt/series
/usr/share/quilt/setup
/usr/share/quilt/snapshot
/usr/share/quilt/top
/usr/share/quilt/unapplied
/usr/share/quilt/upgrade

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/quilt/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/quilt/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/guards.1
/usr/share/man/man1/quilt.1

%files locales -f quilt.lang
%defattr(-,root,root,-)

