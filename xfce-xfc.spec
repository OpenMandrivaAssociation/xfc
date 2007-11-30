%define oname xfc
%define major 1
%define apiversion 4.3
%define libname %mklibname XFC- %{apiversion} %{major}
%define develname %mklibname XFC -d

Summary:	The Xfce foundation classes
Name:		xfce-xfc
Version:	4.3.2
Release:	%mkrel 3
License:	GPL
Group:		Development/C++
Url:		http://xfc.xfce.org
Source0:	http://xfc.xfce.org/download/4.3.2/src/%{oname}-%{version}.tar.bz2
Patch0:		xfc-4.3.2-selection.patch
BuildRequires:	libsigc++2.0-devel
BuildRequires:	libatk-devel
BuildRequires:	libpango-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	libgtksourceview-devel
BuildRequires:	chrpath
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libname}-devel = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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

%package -n demo
Summary:	Xfce foundation classes example files
Group:		Development/Other

%description -n demo
Xfce foundation classes example files.

%package -n %{libname}
Summary:	Xfce foundation classes libraries
Group:		System/Libraries

%description -n %{libname}
Xfce foundation classes libraries.

%package -n %{develname}
Summary:	Xfce foundation classes headers
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}
Provides:	xfce-xfc-devel
Provides:	libXFC-devel
Obsoletes:	%mklibname XFC- %{apiversion} 1 -d

%description -n %{develname}
Xfce foundation classes headers.

%prep
%setup -qn %{oname}-%{version}
%patch0 -p1 -b .selection

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

chrpath -d %{buildroot}%{_bindir}/xfc-demo

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files

%files -n demo
%defattr(-,root,root)
%doc AUTHORS README NEWS COPYING TODO ChangeLog
%{_bindir}/xfc-demo
%{_datadir}/xfce4/xfc/demos/

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXFC*-%{apiversion}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS README NEWS COPYING TODO ChangeLog
%doc %{_docdir}/xfc-4.3/*
%{_includedir}/xfce4/xfc
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_libdir}/xfce4/xfc/include/*.h
