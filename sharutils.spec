%define version 4.6.3
%define release %mkrel 1

Summary:	The GNU shar utilities for packaging and unpackaging shell archives
Name:		sharutils
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Archiving/Backup
Source:		ftp://ftp.gnu.org/pub/gnu/%name/%name-%version.tar.bz2
Url:		http://www.gnu.org/software/sharutils/
#Patch1:		sharutils-4.2-gmo.patch
#Patch2:		sharutils-4.2-man.patch
#Patch3:		sharutils-4.2.1-po.patch
#Patch4:		sharutils-4.2-share.patch
#Patch5:		sharutils-4.2-uudecode.patch
#Patch6:		sharutils-4.2.1-mktemp.patch
#Patch7:		sharutils-4.2.1-uudecode.patch
#Patch10:	sharutils-4.2.1-remsync-typo.patch
#Patch11:	sharutils-4.2.1-bogus-entries.patch
#Patch12:	sharutils-4.2.1-CAN-2004-1772.patch
#Patch13:	sharutils-4.2.1-CAN-2004-1773.patch
#Patch14:	sharutils-4.2.1-deb-302412.patch
Prereq:		/sbin/install-info
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	texinfo

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
%setup -q
#%patch1 -p1 -b .translation-list
#%patch2 -p1 -b .manpath
#%patch3 -p1 -b .po-fix
#%patch4 -p1 -b .localedir
#%patch5 -p1 -b .uudecode
#%patch6 -p1 -b .mktemp
#%patch7 -p1 -b .uudecode2
#%patch10 -p1 -b .func-typo
#%patch11 -p1 -b .info-entry
#%patch12 -p0 -b .can-2004-1772
#%patch13 -p1 -b .can-2004-1772
#%patch14 -p1 -b .302412

%build
%configure

# need not link with libintl explicitly for gettext support
perl -pi -e 's/-lintl//g' src/Makefile

%make

%install
rm -rf $RPM_BUILD_ROOT

# man pages are not installed with make install
#make mandir=$RPM_BUILD_ROOT%{_mandir} install-man
%makeinstall install-man

# fix japanese catalog file
if [ -d $RPM_BUILD_ROOT/%{_datadir}/locale/ja_JP.EUC/LC_MESSAGES ]; then
  pushd $RPM_BUILD_ROOT%{_datadir}/locale
  mv ja_JP.EUC ja
  popd
fi

%find_lang %{name}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,755)
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man?/*


