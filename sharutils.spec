Summary:	The GNU shar utilities for packaging and unpackaging shell archives
Name:		sharutils
Version:	4.11.1
Release:	4
License:	GPLv3
Group:		Archiving/Backup
Url:		http://www.gnu.org/software/sharutils/
Source0:	ftp://ftp.gnu.org/pub/gnu/%name/%name-%version.tar.bz2
Patch0:		sharutils-4.7-fix-str-fmt.patch
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
%patch0 -p0

%build
%configure2_5x \
	--disable-rpath

%make

%install
%makeinstall_std 

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man?/*



%changelog
* Fri Apr 29 2011 Sandro Cazzaniga <kharec@mandriva.org> 4.11.1-1mdv2011.0
+ Revision: 660776
- new version 4.11.1
- update file list
- remove buildroot's definition
- clean %%install

* Sun Feb 06 2011 Sandro Cazzaniga <kharec@mandriva.org> 4.11-1
+ Revision: 636347
- update to 4.11

* Sun Aug 29 2010 Thierry Vignaud <tv@mandriva.org> 4.10-1mdv2011.0
+ Revision: 574101
- new release

* Sun Mar 21 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9-1mdv2010.1
+ Revision: 526234
- update to new version 4.9

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 4.7-7mdv2010.1
+ Revision: 520218
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.7-6mdv2010.0
+ Revision: 427138
- rebuild

* Sun Mar 08 2009 Emmanuel Andry <eandry@mandriva.org> 4.7-5mdv2009.1
+ Revision: 352761
- diff p0 to fix string format not literal

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 4.7-4mdv2009.0
+ Revision: 225438
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 4.7-3mdv2008.1
+ Revision: 179505
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 4.7-2mdv2008.0
+ Revision: 69923
- kill file require on info-install

* Sat Jul 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7-1mdv2008.0
+ Revision: 52024
- spec file clean
- new version


* Sat Jan 06 2007 Emmanuel Andry <eandry@mandriva.org> 4.6.3-1mdv2007.0
+ Revision: 104698
- New version 4.6.3
  %%mkrel
  drop patches
- Import sharutils

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 4.2.1-19mdk
- Rebuild

* Tue Apr 05 2005 Vincent Danen <vdanen@mandrakesoft.com> 4.2.1-18mdk
- P12: security fix for CAN-2004-1772
- P13: security fix for CAN-2004-1773
- P14: security fix for debian bug #302412

* Mon May 24 2004 Abel Cheung <deaddog@deaddog.org> 4.2.1-17mdk
- No need to link with libintl for gettext support
- Fix patch3 (add charset to po files)

* Sat Apr 24 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.2.1-16mdk
- relink against fixed libintl

* Fri Apr 23 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.2.1-15mdk
- relink with new libintl

