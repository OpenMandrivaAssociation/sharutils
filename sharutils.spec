Summary:	The GNU shar utilities for packaging and unpackaging shell archives
Name:		sharutils
Version:	4.15.2
Release:	8
License:	GPLv3
Group:		Archiving/Backup
Url:		http://www.gnu.org/software/sharutils/
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz
# Pass compilation with -Werror=format-security, bug #1037323
Patch0:		%{name}-4.14.2-Pass-compilation-with-Werror-format-security.patch
# Fix CVE-2018-1000097 (a heap buffer overflow in find_archive()),
# bug #1548019,
# <http://lists.gnu.org/archive/html/bug-gnu-utils/2018-02/msg00004.html>
Patch1:		%{name}-4.15.2-Fix-a-heap-buffer-overflow-in-find_archive.patch
# Adapt bundled gnulib to glibc-2.28
Patch2:		%{name}-4.15.2-fflush-adjust-to-glibc-2.28-libio.h-removal.patch
# Fix building with GCC 10,
# <https://lists.gnu.org/archive/html/bug-gnu-utils/2020-01/msg00001.html>
Patch3:		%{name}-4.15.2-Fix-building-with-GCC-10.patch
# Fix building with GCC 10,
# <https://lists.gnu.org/archive/html/bug-gnu-utils/2020-01/msg00001.html>
Patch4:		%{name}-4.15.2-Do-not-include-lib-md5.c-into-src-shar.c.patch

%description
The sharutils package contains the GNU shar utilities, a set of tools
for encoding and decoding packages of files (in binary or text format)
in a special plain text format called shell archives (shar).  This
format can be sent through email (which can be problematic for
regular binary files).  The shar utility supports a wide range of
capabilities (compressing, uuencoding, splitting long files for
multi-part mailings, providing checksums), which make it very flexible
at creating shar files.  After the files have been sent, the unshar
tool scans mail messages looking for shar files.  Unshar automatically
strips off mail headers and introductory text and then unpacks the shar
files.

Install sharutils if you send binary files through email very often.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man?/*
