%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}
Name:           stopmodreposts-utils
Version:        1.0.2
Release:        1%{?dist}
Summary:        StopModReposts internal utilities for maintaining the list

License:        GPL
Source0:        https://github.com/StopModReposts/List-Utils/archive/refs/tags/%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  git


%description
A demo RPM build

%prep
%setup -q -n List-Utils-%{version}

%build
go build -ldflags=-linkmode=external -o smr-list-utils

%install
install -Dm755 smr-list-utils $RPM_BUILD_ROOT/%{_bindir}/smr-list-utils

%files
%{_bindir}/smr-list-utils

%changelog
* Mon Jan 24 2022 dada513 <dada513@protonmail.com> - 1.0.2
- First version being packaged