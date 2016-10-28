Name:		oasis
Version:	0.4.7
Release:	1%{?dist}
Summary:	Architecture for building OCaml libraries and applications

License:	LGPL
URL:		http://oasis.forge.ocamlcore.org/index.html
Source0:	https://github.com/ocaml/oasis/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	ocaml
BuildRequires:	ocaml-camlp4-devel
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocamlify
BuildRequires:	ocamlmod
BuildRequires:	ocaml-ocamldoc
BuildRequires:	ocaml-odn-devel

%description
OASIS generates a full configure, build and install system for your
application. It starts with a simple `_oasis` file at the toplevel of
your project and creates everything required.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-odn-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

# The auto-requirements script mistakenly thinks that the Oasis library
# modules depend on OASISAstTypes.
%{?filter_setup:
%filter_from_requires /OASISAstTypes/d
%filter_setup
}

%prep
%setup -q


%build
./configure --prefix %{_prefix} --destdir %{buildroot}
make


%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install


%files
%{_bindir}/oasis

%{_libdir}/ocaml/plugin-loader/META
%{_libdir}/ocaml/plugin-loader/*.cma
%{_libdir}/ocaml/plugin-loader/*.cmi
%exclude %{_libdir}/ocaml/plugin-loader/*.annot
%exclude %{_libdir}/ocaml/plugin-loader/*.cmt
%exclude %{_libdir}/ocaml/plugin-loader/*.cmti

%{_libdir}/ocaml/oasis/META
%{_libdir}/ocaml/oasis/*.cma
%{_libdir}/ocaml/oasis/*.cmi
%{_libdir}/ocaml/oasis/*.mli
%exclude %{_libdir}/ocaml/oasis/*.annot
%exclude %{_libdir}/ocaml/oasis/*.cmt
%exclude %{_libdir}/ocaml/oasis/*.cmti


%files devel
%{_libdir}/ocaml/plugin-loader/*.a
%{_libdir}/ocaml/plugin-loader/*.cmx
%{_libdir}/ocaml/plugin-loader/*.cmxa
%exclude %{_libdir}/ocaml/plugin-loader/*.cmxs
%exclude %{_libdir}/ocaml/plugin-loader/*.ml

%{_libdir}/ocaml/oasis/*.a
%{_libdir}/ocaml/oasis/*.cmx
%{_libdir}/ocaml/oasis/*.cmxa
%exclude %{_libdir}/ocaml/oasis/*.cmxs
%exclude %{_libdir}/ocaml/oasis/*.ml


%changelog
* Fri Oct 28 2016 Marcello Seri <marcello.seri@citrix.com> - 0.4.7-1
- Update to 0.4.7

* Thu Apr  2 2015 David Scott <dave.scott@citrix.com> - 0.4.5-1
- Update to 0.4.5

* Wed Mar 26 2014 Euan Harris <euan.harris@citrix.com> - 0.4.4-1
- Initial package

