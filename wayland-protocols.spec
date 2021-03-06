Summary:	Wayland protocols that adds functionality not available in the core protocol
Name:		wayland-protocols
Version:	1.21
Release:	1
Group:		Development/C
License:	MIT
URL:		http://wayland.freedesktop.org/
Source0:	http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	pkgconfig(wayland-scanner)

%description
wayland-protocols contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%package devel
Summary:	Wayland protocols that adds functionality not available in the core protocol
Group:		Development/C

%description devel
wayland-protocols contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%prep
%autosetup -p1

%build
%configure

%install
mkdir -p %{buildroot}/%{_libdir}/pkgconfig/
cp %{name}.pc %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc

%make_install

%files devel
%doc README.md
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/*
