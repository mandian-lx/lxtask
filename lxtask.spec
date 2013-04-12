Summary:	Lightweight and desktop independent task manager
Name:		lxtask
Version:	0.1.4
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Patch0:		lxtask-0.1.4-automake_113.patch
URL:		http://lxde.sourceforge.net/
BuildRequires:	gtk+2-devel desktop-file-utils
BuildRequires:	intltool
BuildRequires:	automake

%description
Lightweight and desktop independent task manager.

%prep
%setup -q
%patch0 -p1

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/applications/*.desktop


%changelog
* Fri Apr 29 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.4-1mdv2011.0
+ Revision: 660161
- new release 0.1.4

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-2mdv2011.0
+ Revision: 606447
- rebuild

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 0.1.3-1mdv2010.1
+ Revision: 533695
- new version 0.1.3

* Tue Apr 06 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.1.2-1mdv2010.1
+ Revision: 532086
- new upstream release 0.1.2
- drop fix-desktop-file patch, not needed any more
- add patch to fix fa.po file
- clean spec

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-2mdv2010.1
+ Revision: 523234
- rebuilt for 2010.1

* Fri Jul 10 2009 Funda Wang <fwang@mandriva.org> 0.1.1-1mdv2010.0
+ Revision: 394054
- add BR
- new version 0.1.1

* Tue Dec 16 2008 Funda Wang <fwang@mandriva.org> 0.1-3mdv2009.1
+ Revision: 314834
- update new rel
- add upstream patch to build with new cflags

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.1-2mdv2009.0
+ Revision: 268134
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.1-1mdv2009.0
+ Revision: 200929
- import source
- Created package structure for lxtask.

