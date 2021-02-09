%define major 0
%define libname %mklibname maxflow %{major}
%define develname %mklibname -d maxflow

Name:           maxflow
Version:        3.0.5
Release:        %mkrel 1
Summary:        Software for computing mincut/maxflow in a graph
Group:          System/Libraries
License:        GPLv3+
URL:            https://github.com/gerddie/maxflow
Source0:        https://github.com/gerddie/maxflow/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
This library implements an efficient minimum cut/maximum flow algorithms
on graphs that can be used for exact or approximate energy minimization
in low-level vision. The algorithm provides a high performance that makes
near real-time performance possible.

%package -n     %{libname}
Summary:        A library for %{name}
Group:          System/Libraries

%description -n %{libname}
This library implements an efficient minimum cut/maximum flow algorithms
on graphs that can be used for exact or approximate energy minimization
in low-level vision. The algorithm provides a high performance that makes
near real-time performance possible.

%package -n     %{develname}
Summary:        Header files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This library implements an efficient minimum cut/maximum flow algorithms
on graphs that can be used for exact or approximate energy minimization
in low-level vision. The algorithm provides a high performance that makes
near real-time performance possible.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n %{libname}
%doc CHANGES.TXT README.md
%license GPL.TXT
%{_libdir}/libmaxflow.so.%{major}{,.*}

%files -n %{develname}
%{_libdir}/libmaxflow.so
%{_libdir}/pkgconfig/maxflow.pc
%dir %{_includedir}/maxflow-3.0
%{_includedir}/maxflow-3.0/maxflow.h
%dir %{_includedir}/maxflow-3.0/maxflow
%{_includedir}/maxflow-3.0/maxflow/block.h
%{_includedir}/maxflow-3.0/maxflow/graph.h
%{_includedir}/maxflow-3.0/maxflow/graph.cpp
