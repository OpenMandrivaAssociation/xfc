%define url_ver %(echo %{version} | cut -c 1-3)

%define major 4
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	The Xfce foundation classes
Name:		xfc
Version:	4.6.0
Release:	3
License:	LGPLv2+
Group:		Development/C++
Url:		http://xfc.xfce.org
Source0:	http://archive.xfce.org/src/bindings/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
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

%files doc
%{_docdir}/%{name}-%{version}/docs
%{_docdir}/%{name}-%{version}/tutorial
