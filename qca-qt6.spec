Summary:	Qt Cryptographic Architecture (QCA) Library
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA)
Name:		qca-qt6
Version:	2.3.8
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	https://download.kde.org/stable/qca/%{version}/qca-%{version}.tar.xz
# Source0-md5:	4c6348286c170b3da24820c977565d75
URL:		https://invent.kde.org/libraries/qca
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Qt5Compat-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	cmake >= 2.8.2
BuildRequires:	libstdc++-devel
BuildRequires:	ninja
BuildRequires:	nss-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkcs11-helper-devel
BuildRequires:	qt6-build
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
Requires:	Qt6Core-devel

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
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQCA_INSTALL_IN_QT_PREFIX=ON \
	-DQCA_MAN_INSTALL_DIR=%{_mandir} \
	-DBUILD_WITH_QT6=ON

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
%defattr(644,root,root,755)
%ghost %{_libdir}/libqca-qt6.so.2
%attr(755,root,root) %{_libdir}/libqca-qt6.so.*.*
%attr(755,root,root) %{_libdir}/qt6/bin/mozcerts-qt6
%attr(755,root,root) %{_libdir}/qt6/bin/qcatool-qt6
%dir %{_libdir}/qt6/plugins/crypto
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-cyrus-sasl.so
#%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-gcrypt.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-gnupg.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-logger.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-nss.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-ossl.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-pkcs11.so
%attr(755,root,root) %{_libdir}/qt6/plugins/crypto/libqca-softstore.so
%{_mandir}/man1/qcatool-qt6.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/qt6/Qca-qt6
%{_libdir}/cmake/Qca-qt6
%{_libdir}/libqca-qt6.so
