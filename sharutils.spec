Summary:	The GNU shar utilities for packaging and unpackaging shell archives
Name:		sharutils
Version:	4.11.1
Release:	%mkrel 1
License:	GPLv3
Group:		Archiving/Backup
Url:		http://www.gnu.org/software/sharutils/
Source0:	ftp://ftp.gnu.org/pub/gnu/%name/%name-%version.tar.bz2
Patch0:		sharutils-4.7-fix-str-fmt.patch
Requires(pre):	info-install
BuildRequires:	texinfo
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%patch0 -p0

%build
%configure2_5x \
	--disable-rpath

%make

%install
%makeinstall_std 

%find_lang %{name}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man?/*

