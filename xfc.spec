%define url_ver %(echo %{version} | cut -c 1-3)

%define major 4
#define apiversion %{version}
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	The Xfce foundation classes
Name:		xfc
Version:	4.6.0
Release:	1
License:	LGPLv2+
Group:		Development/C++
Url:		http://xfc.xfce.org
#Source0:	http://archive.xfce.org/src/bindings/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.xz
Patch0:		xfc-4.6.0-rosa-configure.patch
Patch1:		xfc-4.6.0-rosa-glib_h.patch
Patch2:		xfc-4.6.0-rosa-format-security.patch
Patch3:		xfc-4.6.0-rosa-gcc47.patch
Patch4:		xfc-4.6.0-rosa-linkage.patch
Patch5:		xfc-4.6.0-rosa-doxygen.patch
Patch6:		xfc-4.6.0-rosa-libdir.patch
Patch7:		xfc-4.6.0-rosa-docs.patch
Patch8:		xfc-4.6.0-rosa-tutorial.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	chrpath
BuildRequires:	doxygen
Requires:	%{libname} = %{version}
Requires:	%{develname} = %{version}
Requires:	%{name}-demo = %{version}
Requires:	%{name}-doc = %{version}

%description
The Xfce Foundation Classes is a set of integrated C++ classes 
for developing Xfce applications on UNIX-like operating systems 
such as Linux. The classes combine the power of GTK+ and the power 
of C++ into a state-of-the-art application development framework 
for the Xfce Desktop Environment. The classes judiciously use C++ 
language features to avoid layering on too much extra C++ complexity. 
The API is easy to understand and use, and should feel immediately 
familiar to most GTK+ programmers. The Xfce Foundation Classes is part 
of the Xfce project, and like Xfce it's lightweight, fast and easy to use. 

Example files can be found in %{name}-demo package.

%package demo
Summary:	Xfce foundation classes example files
Group:		Development/Other

%description demo
Xfce foundation classes example files.

%package -n %{libname}
Summary:	Xfce foundation classes libraries
Group:		System/Libraries

%description -n %{libname}
Xfce foundation classes libraries.

%package -n %{develname}
Summary:	Xfce foundation classes headers
Group:		Development/C++
Requires:	%{name} = %{version}
Provides:	xfc-devel = %{EVRD}

%description -n %{develname}
Xfce foundation classes headers.

%package doc
Summary:	Xfce foundation classes documentation
Group:		Development/C++

%description doc
Xfce foundation classes documentation.

%prep
%setup -q
%patch0 -p1 -b .configure~
%patch1 -p1 -b .glib~
%patch2 -p1 -b .format~
%patch3 -p1 -b .gcc47~
%patch4 -p1 -b .linkage~
%patch5 -p1 -b .doxygen~
%patch6 -p1 -b .libdir~
%patch7 -p1 -b .docs~
%patch8 -p1 -b .tutorial~

find . -executable  \( -name *.cc -o -name *.hh \) -exec chmod -x {} \;

%build
%cmake

%make

%install
pushd build
%makeinstall_std
popd

chrpath -d %{buildroot}%{_bindir}/xfc-demo

%files

%files demo
%dir %{_datadir}/xfce4/xfc
%{_bindir}/xfc-demo
%{_datadir}/xfce4/xfc/demos

%files -n %{libname}
%{_libdir}/libxfc*.so.%{major}*

%files -n %{develname}
%doc AUTHORS README NEWS TODO ChangeLog
%{_includedir}/xfce4/xfc
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
#%{_libdir}/xfce4/xfc/include/*.h

%files doc
%{_docdir}/%{name}-%{version}/docs
%{_docdir}/%{name}-%{version}/tutorial


%changelog
* Mon Feb 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.3.2-7mdv2008.1
+ Revision: 174776
- fix packaging demo

* Mon Feb 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.3.2-6mdv2008.1
+ Revision: 174521
- do not self-obsolete devel library
- spec file clean

* Sun Feb 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.3.2-5mdv2008.1
+ Revision: 161878
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.3.2-4mdv2008.1
+ Revision: 120499
- fix packaging demo subpackage

* Fri Nov 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.3.2-3mdv2008.1
+ Revision: 114040
- obsolete older name
- do not package COPYING file
- new license policy
- use tarball name as a real name

* Sat Sep 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.3.2-3mdv2008.0
+ Revision: 92130
- rebuild

* Tue Jun 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.3.2-2mdv2008.0
+ Revision: 44304
- new devel library policy
- provide patch 0 (gcc on x86_64 has some problems with cast unsigned char to unsigned int)
- create subpackage demo
- nuke rpath
- Import xfce-xfc

