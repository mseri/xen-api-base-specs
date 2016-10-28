%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-typerep
Version:        113.33.03
Release:        1%{?dist}
Summary:        Runtime types for OCaml.

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/typerep
Source0:        https://ocaml.janestreet.com/ocaml-core/113.33/files/typerep-%{version}.tar.gz
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-js-build-tools-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-bin-prot >= 109.53.02
BuildRequires:  ocaml-sexplib >= 109.55.02
BuildRequires:  ocaml-type-conv

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
Runtime types for OCaml.


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
%setup -q -n typerep-%{version}

%build
make

%check
make test

%install
%__install -D META                                %{buildroot}/%{_libdir}/ocaml/typerep/META
%__install -D _build/lib/typerep_lib.cmx          %{buildroot}/%{_libdir}/ocaml/typerep/typerep_lib.cmx
%__install -D _build/lib/typerep_lib.cmx          %{buildroot}/%{_libdir}/ocaml/typerep/typerep_lib.cmx
%__install -D _build/lib/make_typename.annot      %{buildroot}/%{_libdir}/ocaml/typerep/make_typename.annot
%__install -D _build/lib/make_typename.cmt        %{buildroot}/%{_libdir}/ocaml/typerep/make_typename.cmt
%__install -D _build/lib/make_typename.cmti       %{buildroot}/%{_libdir}/ocaml/typerep/make_typename.cmti
%__install -D _build/lib/named_intf.annot         %{buildroot}/%{_libdir}/ocaml/typerep/named_intf.annot
%__install -D _build/lib/named_intf.cmt           %{buildroot}/%{_libdir}/ocaml/typerep/named_intf.cmt
%__install -D _build/lib/std.annot                %{buildroot}/%{_libdir}/ocaml/typerep/std.annot
%__install -D _build/lib/std.cmt                  %{buildroot}/%{_libdir}/ocaml/typerep/std.cmt
%__install -D _build/lib/std_internal.annot       %{buildroot}/%{_libdir}/ocaml/typerep/std_internal.annot
%__install -D _build/lib/std_internal.cmt         %{buildroot}/%{_libdir}/ocaml/typerep/std_internal.cmt
%__install -D _build/lib/std_internal.cmti        %{buildroot}/%{_libdir}/ocaml/typerep/std_internal.cmti
%__install -D _build/lib/type_abstract.annot      %{buildroot}/%{_libdir}/ocaml/typerep/type_abstract.annot
%__install -D _build/lib/type_abstract.cmt        %{buildroot}/%{_libdir}/ocaml/typerep/type_abstract.cmt
%__install -D _build/lib/type_abstract.cmti       %{buildroot}/%{_libdir}/ocaml/typerep/type_abstract.cmti
%__install -D _build/lib/type_equal.annot         %{buildroot}/%{_libdir}/ocaml/typerep/type_equal.annot
%__install -D _build/lib/type_equal.cmt           %{buildroot}/%{_libdir}/ocaml/typerep/type_equal.cmt
%__install -D _build/lib/type_equal.cmti          %{buildroot}/%{_libdir}/ocaml/typerep/type_equal.cmti
%__install -D _build/lib/type_generic.annot       %{buildroot}/%{_libdir}/ocaml/typerep/type_generic.annot
%__install -D _build/lib/type_generic.cmt         %{buildroot}/%{_libdir}/ocaml/typerep/type_generic.cmt
%__install -D _build/lib/type_generic.cmti        %{buildroot}/%{_libdir}/ocaml/typerep/type_generic.cmti
%__install -D _build/lib/type_generic_intf.annot  %{buildroot}/%{_libdir}/ocaml/typerep/type_generic_intf.annot
%__install -D _build/lib/type_generic_intf.cmt    %{buildroot}/%{_libdir}/ocaml/typerep/type_generic_intf.cmt
%__install -D _build/lib/typename.annot           %{buildroot}/%{_libdir}/ocaml/typerep/typename.annot
%__install -D _build/lib/typename.cmt             %{buildroot}/%{_libdir}/ocaml/typerep/typename.cmt
%__install -D _build/lib/typename.cmti            %{buildroot}/%{_libdir}/ocaml/typerep/typename.cmti
%__install -D _build/lib/typerep_obj.annot        %{buildroot}/%{_libdir}/ocaml/typerep/typerep_obj.annot
%__install -D _build/lib/typerep_obj.cmt          %{buildroot}/%{_libdir}/ocaml/typerep/typerep_obj.cmt
%__install -D _build/lib/typerep_obj.cmti         %{buildroot}/%{_libdir}/ocaml/typerep/typerep_obj.cmti
%__install -D _build/lib/typerepable.annot        %{buildroot}/%{_libdir}/ocaml/typerep/typerepable.annot
%__install -D _build/lib/typerepable.cmt          %{buildroot}/%{_libdir}/ocaml/typerep/typerepable.cmt
%__install -D _build/lib/variant_and_record_intf.annot %{buildroot}/%{_libdir}/ocaml/typerep/variant_and_record_intf.annot
%__install -D _build/lib/variant_and_record_intf.cmt %{buildroot}/%{_libdir}/ocaml/typerep/variant_and_record_intf.cmt
%__install -D _build/lib/typerep_lib.cmxs         %{buildroot}/%{_libdir}/ocaml/typerep/typerep_lib.cmxs
%__install -D _build/lib/typerep_lib.cmi          %{buildroot}/%{_libdir}/ocaml/typerep/typerep_lib.cmi
%__install -D _build/lib/typerep_lib.cmt          %{buildroot}/%{_libdir}/ocaml/typerep/typerep_lib.cmt
%__install -D _build/lib/typerep_lib.a            %{buildroot}/%{_libdir}/ocaml/typerep/typerep_lib.a
%__install -D _build/lib/typerep_lib.cmxa         %{buildroot}/%{_libdir}/ocaml/typerep/typerep_lib.cmxa
%__install -D _build/lib/typerep_lib.cma          %{buildroot}/%{_libdir}/ocaml/typerep/typerep_lib.cma
%__install -D _build/lib/typerep_lib.cmi          %{buildroot}/%{_libdir}/ocaml/typerep/typerep_lib.cmi
%__install -D _build/lib/typerep_lib.cmt          %{buildroot}/%{_libdir}/ocaml/typerep/typerep_lib.cmt


%clean
make clean


%files
%doc LICENSE.txt
%{_libdir}/ocaml/typerep
%exclude %{_libdir}/ocaml/typerep/*.a
%exclude %{_libdir}/ocaml/typerep/*.cmxa
%exclude %{_libdir}/ocaml/typerep/*.cmxs
%exclude %{_libdir}/ocaml/typerep/*.annot
%exclude %{_libdir}/ocaml/typerep/*.cmt
%exclude %{_libdir}/ocaml/typerep/*.cmti


%files devel
%{_libdir}/ocaml/typerep/*.a
%{_libdir}/ocaml/typerep/*.cmxa
%{_libdir}/ocaml/typerep/*.cmxs

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
