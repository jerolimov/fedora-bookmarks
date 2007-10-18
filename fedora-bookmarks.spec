Name:           fedora-bookmarks
Version:        8
Release:        1
Summary:        Fedora bookmarks
Group:          Applications/Internet
License:        GFDL
URL:            http://fedoraproject.org/
Source0:        default-bookmarks.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       system-bookmarks


%description
This package contains the default bookmarks for Fedora.

%prep
# We are nihilists, Lebowski.  We believe in nassing.

%build
# We are nihilists, Lebowski.  We believe in nassing.

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
* Wed Oct 17 2007 Matthias Clasen <mclasen@redhat.com> 8-1
- Update the link to the Fedora project homepage  (#291851)

* Tue Oct  2 2007 Matthias Clasen <mclasen@redhat.com> 7-2
- Remove reference to 'Core' from summary.  (#247362)

* Sun Apr 15 2007 Christopher Aillon <caillon@redhat.com> 7-1
- FC7 bookmarks based on http://fedoraproject.org/wiki/Releases/7/Bookmarks

* Tue Mar 20 2007 Christopher Aillon <caillon@redhat.com> 6-2
- Package review updates

* Wed Oct 18 2006 Christopher Aillon <caillon@redhat.com> 6-1
- Initial version

