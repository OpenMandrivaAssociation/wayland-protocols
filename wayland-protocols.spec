Summary:	Wayland protocols that adds functionality not available in the core protocol
Name:		wayland-protocols
Version:	1.45
Release:	1
Group:		Development/C
License:	MIT
URL:		https://wayland.freedesktop.org/
Source0:	https://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	meson
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
%meson

%meson_build

%install

%meson_install

%files devel
%doc README.md
%{_datadir}/pkgconfig/%{name}.pc
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_includedir}/wayland-protocols/
