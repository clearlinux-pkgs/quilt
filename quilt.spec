#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x865688D038F02FC8 (jdelvare@suse.de)
#
Name     : quilt
Version  : 0.65
Release  : 11
URL      : http://download.savannah.gnu.org/releases/quilt/quilt-0.65.tar.gz
Source0  : http://download.savannah.gnu.org/releases/quilt/quilt-0.65.tar.gz
Source99 : http://download.savannah.gnu.org/releases/quilt/quilt-0.65.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: quilt-bin
Requires: quilt-doc
Requires: quilt-data
Requires: quilt-locales
BuildRequires : ed
BuildRequires : util-linux
Patch1: 0001-test-Escape-curly-braces-in-regex.patch

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
Requires: quilt-data

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

%description doc
doc components for the quilt package.


%package locales
Summary: locales components for the quilt package.
Group: Default

%description locales
locales components for the quilt package.


%prep
%setup -q -n quilt-0.65
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503429775
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1503429775
rm -rf %{buildroot}
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
%defattr(-,root,root,-)
%doc /usr/share/doc/quilt/*
%doc /usr/share/man/man1/*

%files locales -f quilt.lang
%defattr(-,root,root,-)

