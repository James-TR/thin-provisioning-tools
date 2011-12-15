#
# Copyright (C)  2011 Red Hat GmbH. All rights reserved.
#
# See file LICENSE at the top of this source tree for license information.
#

Summary: Device-mapper thin provisioning tools
Name: thin-provisioning-tools
Version: 1.0.0
Release: 1%{?dist}
License: GPLv3
Group: System Environment/Base
URL: http://sources.redhat.com/lvm2
BuildRequires: expat-devel, libstdc++-devel
Source0: ftp://sources.redhat.com/pub/lvm2/thin-provisoning-tools.%{version}.tgz
Requires: expat, libstdc++

%description
thin-provisioning-tools contains dump,restore and repair tools to
manage device-mapper thin provisioning target metadata devices.

%prep
%setup -q -n thin-provisioning-tools.%{version}

%build
%define _exec_prefix ""
%define _bindir /bin
%define _sbindir /usr/sbin
%define _libdir /%{_lib}

%configure

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING COPYING.LIB INSTALL README VERSION WHATS_NEW
/%{_mandir}/man8/thin_dump.8.gz
/%{_mandir}/man8/thin_repair.8.gz
/%{_mandir}/man8/thin_restore.8.gz
%{_sbindir}/thin_dump
%{_sbindir}/thin_repair
%{_sbindir}/thin_restore

%changelog
* Thu Dec 15 2011  Heinz Mauelshagen <heinzm@redhat.com> - 1.0.0-1
- Initial version
