Summary:	Qt Cryptographic Architecture (QCA) Library
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA)
Name:		qca-qt6
Version:	2.3.9
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	https://download.kde.org/stable/qca/%{version}/qca-%{version}.tar.xz
# Source0-md5:	d8aaa46356a322464f65b04d00d2bac6
URL:		https://invent.kde.org/libraries/qca
BuildRequires:	Qt6Core-devel >= 6
BuildRequires:	Qt6Qt5Compat-devel >= 6
BuildRequires:	Qt6Test-devel >= 6
# or botan3 (with C++20)
BuildRequires:	botan2-devel >= 2
BuildRequires:	cmake >= 3.16
BuildRequires:	cyrus-sasl-devel >= 2
BuildRequires:	libgcrypt-devel
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	ninja
BuildRequires:	nss-devel
BuildRequires:	openssl-devel >= 1.1.1
BuildRequires:	pkcs11-helper-devel
BuildRequires:	qt6-build >= 6
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Cryptographic Architecture (QCA) Library.

%description -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA).

%package devel
Summary:	Qt Cryptographic Architecture (QCA) Library - development files
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= 6
Requires:	libstdc++-devel >= 6:7

%description devel
Qt Cryptographic Architecture (QCA) Library - development files.

%description devel -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla
programistów.

%prep
%setup -q -n qca-%{version}

%build
export LC_ALL=C.UTF-8
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTS=OFF} \
	-DBUILD_WITH_QT6=ON \
	-DQCA_INSTALL_IN_QT_PREFIX=ON \
	-DQCA_MAN_INSTALL_DIR=%{_mandir}

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libqca-qt6.so.*.*.*
%ghost %{_libdir}/libqca-qt6.so.2
%attr(755,root,root) %{_libdir}/qt6/bin/mozcerts-qt6
%attr(755,root,root) %{_libdir}/qt6/bin/qcatool-qt6
%dir %{_libdir}/qt6/plugins/crypto
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-botan.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-cyrus-sasl.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-gcrypt.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-gnupg.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-logger.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-nss.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-ossl.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-pkcs11.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-softstore.so
%{_mandir}/man1/qcatool-qt6.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libqca-qt6.so
%{_includedir}/qt6/Qca-qt6
%{_libdir}/cmake/Qca-qt6
