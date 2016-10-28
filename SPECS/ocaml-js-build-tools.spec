%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-js-build-tools
Version:        113.33.06
Release:        1%{?dist}
Summary:        Jane Street Build Tools goodies for OCaml.

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/js-build-tools
Source0:        https://ocaml.janestreet.com/ocaml-core/113.33/files/js-build-tools-%{version}.tar.gz
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml
BuildRequires:  oasis
BuildRequires:  ocaml-findlib-devel

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
Jane Street Build Tools goodies for OCaml.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-sexplib
Requires:       ocaml-bin-prot
Requires:       ocaml-type-conv

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n js-build-tools-%{version}

%build
make

%check
make test

%install
%__install -D META %{buildroot}/%{_libdir}/ocaml/js-build-tools/META
%__install -D _build/oasis2opam-install/oasis2opam_install.cmx %{buildroot}/%{_libdir}/ocaml/js-build-tools/oasis2opam_install.cmx
%__install -D _build/oasis2opam-install/oasis2opam_install.annot %{buildroot}/%{_libdir}/ocaml/js-build-tools/oasis2opam_install.annot
%__install -D _build/oasis2opam-install/oasis2opam_install.cmt %{buildroot}/%{_libdir}/ocaml/js-build-tools/oasis2opam_install.cmt
%__install -D _build/oasis2opam-install/oasis2opam_install.cmti %{buildroot}/%{_libdir}/ocaml/js-build-tools/oasis2opam_install.cmti
%__install -D _build/oasis2opam-install/oasis2opam_install.cmi %{buildroot}/%{_libdir}/ocaml/js-build-tools/oasis2opam_install.cmi
%__install -D _build/oasis2opam-install/oasis2opam_install.cmxs %{buildroot}/%{_libdir}/ocaml/js-build-tools/oasis2opam_install.cmxs
%__install -D _build/oasis2opam-install/oasis2opam_install.a %{buildroot}/%{_libdir}/ocaml/js-build-tools/oasis2opam_install.a
%__install -D _build/oasis2opam-install/oasis2opam_install.cmxa %{buildroot}/%{_libdir}/ocaml/js-build-tools/oasis2opam_install.cmxa
%__install -D _build/oasis2opam-install/oasis2opam_install.cma %{buildroot}/%{_libdir}/ocaml/js-build-tools/oasis2opam_install.cma
%__install -D _build/ocamlbuild_goodies/jane_street_ocamlbuild_goodies.cmx %{buildroot}/%{_libdir}/ocaml/js-build-tools/jane_street_ocamlbuild_goodies.cmx
%__install -D _build/ocamlbuild_goodies/jane_street_ocamlbuild_goodies.annot %{buildroot}/%{_libdir}/ocaml/js-build-tools/jane_street_ocamlbuild_goodies.annot
%__install -D _build/ocamlbuild_goodies/jane_street_ocamlbuild_goodies.cmt %{buildroot}/%{_libdir}/ocaml/js-build-tools/jane_street_ocamlbuild_goodies.cmt
%__install -D _build/ocamlbuild_goodies/jane_street_ocamlbuild_goodies.cmti %{buildroot}/%{_libdir}/ocaml/js-build-tools/jane_street_ocamlbuild_goodies.cmti
%__install -D _build/ocamlbuild_goodies/jane_street_ocamlbuild_goodies.cmi %{buildroot}/%{_libdir}/ocaml/js-build-tools/jane_street_ocamlbuild_goodies.cmi
%__install -D _build/ocamlbuild_goodies/jane_street_ocamlbuild_goodies.cmxs %{buildroot}/%{_libdir}/ocaml/js-build-tools/jane_street_ocamlbuild_goodies.cmxs
%__install -D _build/ocamlbuild_goodies/jane_street_ocamlbuild_goodies.a %{buildroot}/%{_libdir}/ocaml/js-build-tools/jane_street_ocamlbuild_goodies.a
%__install -D _build/ocamlbuild_goodies/jane_street_ocamlbuild_goodies.cmxa %{buildroot}/%{_libdir}/ocaml/js-build-tools/jane_street_ocamlbuild_goodies.cmxa
%__install -D _build/ocamlbuild_goodies/jane_street_ocamlbuild_goodies.cma %{buildroot}/%{_libdir}/ocaml/js-build-tools/jane_street_ocamlbuild_goodies.cma


%clean
make clean

%files
%doc LICENSE.txt README.md
%{_libdir}/ocaml/js-build-tools
%exclude %{_libdir}/ocaml/js-build-tools/*.a
%exclude %{_libdir}/ocaml/js-build-tools/*.cmxa
%exclude %{_libdir}/ocaml/js-build-tools/*.cmxs
%exclude %{_libdir}/ocaml/js-build-tools/*.annot
%exclude %{_libdir}/ocaml/js-build-tools/*.cmt
%exclude %{_libdir}/ocaml/js-build-tools/*.cmti


%files devel
%{_libdir}/ocaml/js-build-tools/*.a
%{_libdir}/ocaml/js-build-tools/*.cmxa
%{_libdir}/ocaml/js-build-tools/*.cmxs

%changelog
* Fri Oct 28 2016 Marcello Seri <marcello.seri@citrix.com> - 113.33.03-1
- Update to 113.33.03

* Wed Jul 27 2016 Euan Harris <euan.harris@citrix.com> - 112.35.00-2
- Remove *.cmt, *.cmti and *.annot

* Fri Jan 22 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 112.35.00-1
- Update to 112.35.00

* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 111.17.00-1
- Update to 111.17.00

* Wed Jan 01 2014 Edvard Fagerholm <edvard.fagerholm@gmail.com> - 109.55.02-1
- Initial package for Fedora 20.
