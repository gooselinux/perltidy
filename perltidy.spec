Name:           perltidy
Version:        20090616
Release:        2.1%{?dist}
Summary:        Tool for indenting and reformatting Perl scripts

Group:          Development/Tools
License:        GPLv2+
URL:            http://perltidy.sourceforge.net/
Source:         http://downloads.sourceforge.net/perltidy/Perl-Tidy-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Perltidy is a Perl script which indents and reformats Perl scripts to
make them easier to read. If you write Perl scripts, or spend much
time reading them, you will probably find it useful.  The formatting
can be controlled with command line parameters.  The default parameter
settings approximately follow the suggestions in the Perl Style Guide.
Perltidy can also output html of both pod and source code.  Besides
reformatting scripts, Perltidy can be a great help in tracking down
errors with missing or extra braces, parentheses, and square brackets
because it is very good at localizing errors.


%prep
%setup -q -n Perl-Tidy-%{version}
rm -f docs/perltidy.1 examples/pt.bat
f=CHANGES ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc BUGS CHANGES COPYING README TODO docs/ examples/
%{_bindir}/perltidy
%{perl_vendorlib}/Perl/
%{_mandir}/man1/perltidy.1*
%{_mandir}/man3/Perl::Tidy.3*


%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 20090616-2.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090616-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Ville Skyttä <ville.skytta at iki.fi> - 20090616-1
- Update to 20090616.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071205-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 20071205-3
- Rebuild for perl 5.10 (again)

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 20071205-2
- rebuild for new perl

* Thu Dec  6 2007 Ville Skyttä <ville.skytta at iki.fi> - 20071205-1
- 20071205.
- Convert docs to UTF-8.

* Wed Aug  1 2007 Ville Skyttä <ville.skytta at iki.fi> - 20070801-1
- 20070801.

* Wed May  9 2007 Ville Skyttä <ville.skytta at iki.fi> - 20070508-1
- 20070508.

* Sat May  5 2007 Ville Skyttä <ville.skytta at iki.fi> - 20070504-1
- 20070504.

* Tue Apr 24 2007 Ville Skyttä <ville.skytta at iki.fi> - 20070424-1
- 20070424.

* Tue Apr 17 2007 Ville Skyttä <ville.skytta at iki.fi> - 20060719-3
- BuildRequire perl(ExtUtils::MakeMaker).

* Fri Sep 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 20060719-2
- Rebuild.

* Thu Jul 20 2006 Ville Skyttä <ville.skytta at iki.fi> - 20060719-1
- 20060719.
- Fix order of options to find(1) in %%install.

* Thu Jun 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 20060614-1
- 20060614, specfile cleanups, include examples in docs.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Dec 16 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:20031021-1
- Sync with fedora-rpmdevtools' Perl spec template to fix x86_64 build.
- Move version to the version field.

* Wed Oct 22 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.3.20031021
- Update to 20031021.

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.3.20030726
- Install into vendor dirs.
- Spec cleanups.

* Tue Jul 29 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.2.20030726
- Update to 20030726.
- Use fedora-rpm-helper.

* Mon Jun 23 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.2.20021130
- Address issues in #194:
- Patch to get rid of a warning on startup.
- Do defattr before doc.

* Fri May 30 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20021130
- Fix release naming scheme (this is snapshot-only).

* Wed May  7 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.0.2.20021130
- Own dirs.
- Save .spec in UTF-8.

* Mon Apr 21 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.0.1.20021130
- First Fedora release, based on Simon Perreault's work.

* Mon Mar 10 2003 Simon Perreault <nomis80@nomis80.org> 20021130-2
- Changed architecture from i386 to noarch
- Added my name as packager
- Bumped up release number, which was forgotten by Anthony Rumble

* Sun Mar 09 2003 Anthony Rumble <anthony@linuxhelp.com.au>
- Tidied up RPM Source

* Sun Dec  1 2002 Simon Perreault <nomis80@linuxquebec.com>
- Update to 20021130

* Sat Nov  9 2002 Simon Perreault <nomis80@linuxquebec.com>
- Update to 20021106

* Mon Sep 23 2002 Simon Perreault <nomis80@linuxquebec.com>
- Update to 20020922

* Wed Aug 28 2002 Simon Perreault <nomis80@linuxquebec.com>
- Update to 20020826

* Tue May 7 2002 Simon Perreault <nomis80@linuxquebec.com>
- Require 5.6.1 because Tidy.pm is placed in a directory dependant on perl
  version.

* Sat Apr 27 2002 Simon Perreault <nomis80@linuxquebec.com>
- Update to 20020425.

* Wed Apr 17 2002 Simon Perreault <nomis80@linuxquebec.com>
- Generalized spec file. Added some documentation.

* Wed Apr 17 2002 Simon Perreault <nomis80@linuxquebec.com>
- Upgraded to version 20020416

* Mon Feb 25 2002 Simon Perreault <nomis80@linuxquebec.com>
- Spec file was created on release of 20020225
