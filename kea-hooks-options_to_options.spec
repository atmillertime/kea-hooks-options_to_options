#http://lists.fedoraproject.org/pipermail/devel/2011-August/155358.html
%global _hardened_build 1

#global prever P1

Name:           kea-hooks-options_to_options
Version:        1.0.0
Release:        1%{?dist}
Summary:        A kea hook for templating options

License:        MPLv2.0 and Boost
URL:            https://github.com/funzoneq/kea-hooks-options_to_options
Source0:	https://github.com/funzoneq/kea-hooks-options_to_options/archive/kea-hooks-options_to_options-%{version}.tar.gz

# autoreconf
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: boost-devel
BuildRequires: gtest-devel
BuildRequires: gcc-c++
BuildRequires: systemd
BuildRequires: kea
BuildRequires: kea-hooks
BuildRequires: kea-devel
BuildRequires: kea-libs

%description
This hook takes the value from different options in a DHCPREQUEST and inserts them into (other) options in a DHCPREPLY

%prep
%autosetup -n kea-hooks-options_to_options-%{version}

%build
autoreconf --verbose --force --install
export CXXFLAGS="%{optflags} -std=gnu++11 -Wno-deprecated-declarations"

%configure \

%make_build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/hooks/
cp /builddir/build/BUILD/kea-hooks-options_to_options-%{version}/.libs/options_to_options.so $RPM_BUILD_ROOT%{_libdir}/hooks/

%files
%{_libdir}/hooks/options_to_options.so

%changelog
* Wed Feb 20 2019 Arnoud Vermeer <arnoud@openfiber.net> - 1.0.0-1
- initial spec
